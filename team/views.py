from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Sum, Avg, Value
from django.db.models.functions import Coalesce
from team.models import Member
import time
from fitness.models import Ride, Incident

@login_required
def fitnessStats(request):
    # aggregate
    totalMiles = Ride.objects.all().aggregate(Sum('miles'))['miles__sum']
    totalTime = Ride.objects.all().aggregate(Sum('duration'))['duration__sum']

    # Individual
    riders = Member.objects
    riders = riders.annotate(total_miles = Coalesce(Sum('rider__miles'), 0))
    riders = riders.annotate(total_time = Sum('rider__duration'))
    riders = riders.order_by('-total_miles')

    context = {
        'riders': riders,
        'totalMiles': totalMiles,
        'totalTime': totalTime
    }

    return render(request, 'team/fitness_stats.html', context)

@login_required
def teamDirectory(request):
    # Get all the team info
    teammates = Member.objects
    teammates = teammates.order_by('first_name')

    context = {
        'teammates': teammates,
    }

    return render(request, 'team/directory.html', context)