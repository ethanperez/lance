from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from fitness.models import Ride

def viewLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard:dashboard'))
            else:
                context = {
                    'alert_title': 'Login Error',
                    'alert_message': 'This is not an active account.'
                }
                return render(request, 'dashboard/login.html', context)
        else:
            context = {
                    'alert_title': 'Login Error',
                    'alert_message': 'Invalid username or password.'
                }
            return render(request, 'dashboard/login.html', context)
    else:
        return render(request, 'dashboard/login.html')

@login_required
def viewLogout(request):
    logout(request)
    return(redirect('dashboard:login'))

@login_required
def dashboard(request):
    # Rides
    rides = Ride.objects.filter(member_id__exact = request.user).order_by('-date')
    recent_rides = Ride.objects.filter(member_id__exact = request.user).order_by('-date')[:5]
    miles = rides.aggregate(Sum('miles'))
    duration = rides.aggregate(Sum('duration'))


    context = {
        'rides': rides,
        'recent_rides': recent_rides,
        'total_miles': miles,
        'total_duration': duration
    }

    return render(request, 'dashboard/dashboard.html', context)