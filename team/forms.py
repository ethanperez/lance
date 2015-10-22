from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from team.models import Member

class MemberCreationForm(forms.ModelForm):
  """
    Admin form for creating new users.
    Includes vital fields.
  """
  password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
  password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput)
 
  class Meta:
    model = Member
    fields = ('email', 'first_name', 'last_name', 'is_rider', 'is_staff')

  def clean_password2(self):
    """
      Checks for matching password
      and password confirmation
    """
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('The passwords don\'t match!')
    return password2

  def save(self, commit = True):
    """
      Save the hashed passwords
    """
    member = super(MemberCreationForm, self).save(commit = False)
    member.set_password(self.cleaned_data['password1'])
    if commit:
      member.save()
    return member

class MemberChangeForm(forms.ModelForm):
  """
    Admin form for updating users.
    Includes all fields.
  """
  password = ReadOnlyPasswordHashField()

  class Meta:
    model = Member
    fields = '__all__'

  def clean_password(self):
    return self.initial['password']