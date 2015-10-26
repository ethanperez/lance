from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Sum, Avg
from team.models import Member
import time
from fitness.models import Ride

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
        group = request.POST['rideGroup']
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
        return render(request, 'fitness/addRide.html')