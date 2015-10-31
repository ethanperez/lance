from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Sum, Avg
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
    riders = riders.annotate(total_miles = Sum('rider__miles'))
    riders = riders.annotate(total_time = Sum('rider__duration'))
    riders = riders.order_by('-total_miles')

    context = {
        'riders': riders,
        'totalMiles': totalMiles,
        'totalTime': totalTime
    }

    return render(request, 'team/fitness_stats.html', context)