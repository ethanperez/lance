from django.teset import TestCase
from team.models import Member
from fitness.models import Ride
from django.test import Client
from timezone import now

class TestFitnessModel(TestCase):
  
  def setUp(self):
    # Create user
    user = Member.objects.create_user('normal@test.com', 'Normal', 'Me', 'normal')
    # Create rides
    Ride.objects.create(
      member = user,
      date = now(),
      group_members = "Mike, Kevin, James",
      miles = 123.22,
      pace = 12.22,
      duration = 10:10:10,
      comments = "It was a ride"
    )

  def testGetRide(self):
    testRide = Ride.objects.get(member = user)
    assertEqual(testRide.miles, 123.22)

    