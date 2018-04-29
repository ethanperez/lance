from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
import boto3
from botocore.exceptions import ClientError

from django.db.models import Sum, Avg
from team.models import Member
import time
import os
import io
from fitness.models import Ride, Incident

# Create your views here.
@login_required
def viewAllRides(request):
    # Retreive all of the mile records
    rides = Ride.objects.filter(member_id__exact = request.user).order_by('-date')
    miles = rides.aggregate(Sum('miles'))
    pace = rides.aggregate(Avg('pace'))
    duration = rides.aggregate(Sum('duration'))

    # Context
    context = {
        'rides': rides,
        'total_miles': miles,
        'avg_pace': pace,
        'total_duration': duration,
        'rider': request.user
    }

    return render(request, 'fitness/viewAll.html', context)

@login_required
def logRide(request):
    if request.method == 'POST':
        group = ', '.join(request.POST.getlist('rideGroup[]'))
        miles = request.POST['rideMiles']
        pace = request.POST['ridePace']
        comments = request.POST['rideComments']
        date = request.POST['rideDate']
        logged_time = request.POST['rideTime']

        # Save to the database
        try:
            object = Ride.objects.create(
                    member_id = request.user.id,
                    date = date,
                    group_members = group,
                    miles = miles,
                    pace = pace,
                    duration = logged_time,
                    comments = comments
            )
            object.save()
        except:
            context = {
                'alert_title': 'Save failed!',
                'alert_message': 'It seems like there was an error saving your ride. Try again.'
            }
            return render(request, 'fitness/addRide.html', context)

        return HttpResponseRedirect(reverse('fitness:allRides'))
    else:
        teammates = Member.objects
        teammates = teammates.order_by('first_name')

        context = {
            'teammates': teammates,
        }

        return render(request, 'fitness/addRide.html', context)

@login_required
def viewAllIncidents(request):
    # Retreive all of the mile records
    incidents = Incident.objects.filter(member_id__exact = request.user).order_by('-incident_date')

    # Context
    context = {
        'incidents': incidents,

    }

    return render(request, 'fitness/viewIncidents.html', context)

@login_required
def logIncident(request):
    if request.method == 'POST':
        date = request.POST['incidentDate'] + " " + request.POST['incidentTime']
        event = request.POST['incidentEvent']
        location = request.POST['incidentLocation']
        incident_description = request.POST['incidentDescription']
        surrounding_description = request.POST['surroundingsDescription']
        witnesses = request.POST.get('incidentWitness', default = None)
        responders = request.POST.get('incidentResponders', default = None)
        injuries = request.POST.get('incidentInjury', default = None)
        first_aid = request.POST.get('incidentFirstAid', default = None)
        follow_up = request.POST.get('incidentFollowUp', default = None)

        # Save to the database
        try:
            object = Incident.objects.create(
                member_id = request.user.id,
                incident_date = date,
                event = event,
                incident_location = location,
                incident_description = incident_description,
                surrounding_description = surrounding_description,
                witnesses = witnesses,
                responders = responders,
                injuries = injuries,
                first_aid = first_aid,
                follow_up = follow_up
            )
            object.save()
        except:
            context = {
                'alert_title': 'Save failed!',
                'alert_message': 'It seems like there was an error saving your incident. Try again.'
            }
            return render(request, 'fitness/addIncident.html', context)

        # We've saved, now try to email
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        SENDER = "Texas 4000 RMS <notifications@t4k.pw>"

        # Replace recipient@example.com with a "To" address. If your account
        # is still in the sandbox, this address must be verified.
        RECIPIENT = "ethan@ethanperez.com"

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "us-east-1"

        # The subject line for the email.
        FILING_USER = Member.objects.get(id = request.user.id)
        SUBJECT = "{} has filed an incident report"

        # The HTML body of the email.
        BODY_HTML = """<html>
        <head></head>
        <body>
        <p>
            You can view the report <a href='{}/fitness/incidents/{}/pdf/'>here</a>.
        </p>
        </body>
        </html>
        """
        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML.format(request.get_host(), object.id),
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT.format(FILING_USER.get_full_name()),
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['ResponseMetadata']['RequestId'])

        return HttpResponseRedirect(reverse('fitness:allIncidents'))
    else:
        return render(request, 'fitness/addIncident.html')

@login_required
def viewIncident(request, incident = None):
    # Get the incident
    inc = Incident.objects.get(id = incident)
    # Send it away
    context = {
        'incident': inc,
    }

    return render(request, 'fitness/viewIncident.html', context)

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

@login_required
def viewIncidentPdf(request, incident = None):
    # Get the incident
    resp = HttpResponse(content_type = 'application/pdf')
    inc = Incident.objects.get(id = incident)
    # Send it away
    context = {
        'incident': inc,
    }

    # Render html content through html template with context
    template = get_template('fitness/viewIncidentPDF.html')
    html = template.render(Context(context))

    # Write PDF to file
    file = io.BytesIO()
    pisaStatus = pisa.CreatePDF(html, dest = file, link_callback = link_callback)

    # Return PDF document through a Django HTTP response
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, content_type = 'application/pdf')
