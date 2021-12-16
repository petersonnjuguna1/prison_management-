from django.db.models import fields
from .models import *
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class DateInput(forms.DateInput):
    input_type='date'

# user registration form creation
class PrisonerRegForm(UserCreationForm):
    fullname=forms.CharField(max_length=40)
    # email=forms.EmailField(required=True)
    # phoneno=forms.IntegerField()
    # PNo=forms.IntegerField(blank=True, editable=False)
    dob=forms.DateField()
    marital=forms.CharField(max_length=10)
    gender=forms.CharField(max_length=10)
    # image=forms.ImageField(required=False)
    
    class Meta:
        model=User
        fields=['username','fullname','dob','marital','gender','password1','password2']
        
        
        widgets={
            'dob':DateInput(),
        }
        
        
class VisitorRegForm(UserCreationForm):
    # email=forms.EmailField(required=True)
    # phoneno=forms.IntegerField()
    # fullname=forms.CharField(max_length=40)
    # address=forms.CharField(max_length=40)
    # date=forms.DateField()
    # relationship=forms.CharField(max_length=40)
    
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class VisitorAccountForm(forms.ModelForm):
  
    class Meta:
        model=visitorsprofile
        fields='__all__'
        
        widgets={
            'date':DateInput(),
        }    
        
          
class CreateVisitationForm(forms.ModelForm):
    class Meta:
        model=Visitation
        fields='__all__'
        exclude=['status','prisoner','phoneNo']
        
        widgets={
            'visitationdate':DateInput(),
            'date':DateInput(),
        }

class CreatePrisonerForm(forms.ModelForm):
    class Meta:
        model=Prisonerdetails
        fields='__all__'
        exclude=['prisoner']
        
        widgets={
            'datein':DateInput(),
            'dateout':DateInput(),
        }
class PrisonerAccountForm(forms.ModelForm):
    class Meta:
        model=Prisonerprofile
        fields='__all__'
        exclude=['username']