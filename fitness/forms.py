from django.forms import ModelForm
from .models import Ride, Incident

class RideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['date', 'group_members', 'miles', 'pace', 'duration', 'comments']