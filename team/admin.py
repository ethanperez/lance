from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from team.models import Member
from team.forms import MemberCreationForm, MemberChangeForm

class MemberAdmin(UserAdmin):
  """
    Define the forms and layout of the
    user admin page
  """
  form = MemberChangeForm
  add_form = MemberCreationForm

  # Fields to display in table of all members
  list_display = ('get_full_name', 'email', 'route', 'is_staff')
  list_filter = ('is_staff', 'route')

  # Layout of change member page
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal Information', {'fields': ('first_name', 'last_name', 
      'address_line1', 'address_line2', 'address_zip', 'date_of_birth',
      'site_rider_url', 'site_photo_url')}),
    ('Team Information', {'fields': ('route', 'is_rider', 'is_staff')}),
    ('Permissions', {'fields': ('is_active', 'is_superuser',
      'groups', 'user_permissions')}),
  )

  # Layout of add member page
  add_fieldsets = (
    (None, {'classes': ('wide,'),
    'fields': ('email', 'first_name', 'last_name',
      'password1', 'password2')}
    ),
  )

  # Search fields
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('first_name', 'last_name')
  filter_horizontal = ('groups', 'user_permissions')

admin.site.register(Member, MemberAdmin)
