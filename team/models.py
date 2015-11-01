from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MemberManager(BaseUserManager):
  """
    Manager class that controls the creation of new members
  """
  def _create_user(self, email, first_name, last_name, password,
                  is_rider, is_staff, is_superuser, **extra_fields):
    """
      Base method to create a new user
    """
    # set the timezone
    now = timezone.now()
    # Validate for email
    if not email:
      raise ValueError('User must have an email')

    # Assign data
    member = self.model(
      email = self.normalize_email(email),
      first_name = first_name,
      last_name = last_name,
      is_active = True,
      is_staff = is_staff,
      is_rider = is_rider,
      is_superuser = is_superuser,
      date_joined = now
    )

    # Set password and save record
    member.set_password(password)
    member.save(using = self._db)

    return member

  def create_user(self, email, first_name, last_name, password, **extra_fields):
    """
      Create a standard user (rider)
    """
    return self._create_user(email, first_name, last_name, password, True, False, False, **extra_fields)

  def create_superuser(self, email, first_name, last_name, password, **extra_fields):
    """
      Create a superuser
    """
    return self._create_user(email, first_name, last_name, password, False, True, True, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
  """
    Member model"
  """
  email = models.EmailField('email address', max_length = 100, unique = True, db_index = True)
  first_name = models.CharField('first name', max_length = 35)
  last_name = models.CharField('last name', max_length = 35)

  # Choices for route field
  ROUTE_CHOICES = (
    ('none', 'None (staff)'),
    ('sierra', 'Sierra'),
    ('rockies', 'Rockies'),
    ('ozarks', 'Ozarks')
  )

  route = models.CharField(max_length = 8, choices = ROUTE_CHOICES, default = 'none')
  date_of_birth = models.DateField('date of birth', null = True, blank = True)
  is_active = models.BooleanField('active status', default = True)
  is_rider = models.BooleanField('is on current team', default = True)
  is_staff = models.BooleanField('member of leadership', default = False)
  date_joined = models.DateTimeField('date joined', default = timezone.now)
  # T4K website-only data
  site_rider_url = models.CharField(max_length = 200, blank = True)
  site_photo_url = models.URLField(blank = True)
  # Incident resporting items
  phone = models.BigIntegerField(null = True)
  address_line1 = models.CharField(max_length = 100, blank = True)
  address_line2 = models.CharField(max_length = 100, blank = True)
  address_zip = models.IntegerField(null = True)

  # Class manager
  objects = MemberManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  # Meta
  class Meta:
    verbose_name = 'member'
    verbose_name_plural = 'members'

  # Required methods
  def get_full_name(self):
    full_name ="{0} {1}".format(self.first_name, self.last_name)
    return full_name.strip()
  get_full_name.short_description = 'Name'

  def get_short_name(self):
    return self.first_name

  def get_phone(self):
    try:
      new_phone = str(self.phone)
      return "(" + new_phone[0:3] + ") " + new_phone[3:6] + " - " + new_phone[6:]
    except:
      return self.phone

  def __str__(self):
    return self.get_full_name()