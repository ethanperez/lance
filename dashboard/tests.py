import unittest
from django.test import TestCase
from team.models import Member
from django.test import Client

class TestAuth(TestCase):

  def setUp(self):
    # Create test client.
    self.client = Client()
    superMember = Member.objects.create_superuser('super@test.com', 'Super', 'Me', 'super')
    normalMember = Member.objects.create_user('normal@test.com', 'Normal', 'Me', 'normal') 

  '''
    LOGIN TESTS
  '''
  # Test ability to access dashboard
  def testLoginPageAccess(self):
    response = self.client.get('/login/')

    # Page loaded
    self.assertEqual(response.status_code, 200)

  # Test superuser login and logout
  def testSuperLifeCycle(self):
    # Login
    response = self.client.login(username = 'super@test.com', password = 'super')
    self.assertEqual(response, True)

    # Logout
    self.client.logout()

    # Try to access restrictd area
    response = self.client.get('/', follow = True)

    # Assert redirect to login
    self.assertEqual(response.redirect_chain[0][0], 'http://testserver/login/?next=/')
    # Assert 302 redirect status code
    self.assertEqual(response.redirect_chain[0][1], 302)

  # Test normal user login and logout
  def testNormalLifeCycle(self):
    # Login
    response = self.client.login(username = 'normal@test.com', password = 'normal')
    self.assertEqual(response, True)

    # Logout
    self.client.logout()

    # Try to access restrictd area
    response = self.client.get('/', follow = True)

    # Assert redirect to login
    self.assertEqual(response.redirect_chain[0][0], 'http://testserver/login/?next=/')
    # Assert 302 redirect status code
    self.assertEqual(response.redirect_chain[0][1], 302)