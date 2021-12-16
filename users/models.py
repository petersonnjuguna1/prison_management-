from django.db import models
# from django.db.models.enums import Choices
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth import get_user_model




# prisoner profile
class Prisonerprofile(models.Model):
    user=models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    
    fullname=models.CharField(max_length=40,null=True)
    username=models.CharField(max_length=40,null=True)
    dob=models.DateTimeField(null=True)
    marital=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    # image=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.fullname or ''

#add a user automatically to the database when created.
@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Prisonerprofile.objects.create(user=instance)
    try:
        instance.prisonerprofile.save()
    except ObjectDoesNotExist:
        Prisonerprofile.objects.create(user=instance)


class Prisonerdetails(models.Model): 
    user=models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
    
    prisoner=models.ForeignKey('prisonerprofile',null=True, blank=True, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=40,null=True)
    
    PNo=models.IntegerField(blank=True,null=True)
    # address=models.CharField(max_length=40,null=True)
    offence=models.CharField(max_length=40,null=True)
    sentence=models.IntegerField(null=True)
    # prison=models.CharField(max_length=40,null=True)
    datein=models.DateTimeField( max_length=40,null=True)
    dateout=models.DateTimeField(max_length=40,null=True)
    # image=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.prisoner or ''
    


class visitorsprofile(models.Model): 
    user=models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=40,null=True)
    
    address=models.CharField(max_length=40,null=True)
    phoneNo=models.CharField(max_length=13,null=True, unique=True)
    date=models.DateTimeField(max_length=40,null=True)
    relationship=models.CharField(max_length=40,null=True)
    
    def __str__(self):
        return self.fullname or ''
    
    
@receiver(post_save, sender=User)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        visitorsprofile.objects.create(user=instance)
    try:
        instance.visitorsprofile.save()
    except ObjectDoesNotExist:
        visitorsprofile.objects.create(user=instance)


class Visitation(models.Model):
    user=models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE )
    visitor=models.ForeignKey(visitorsprofile,null=True, blank=True, on_delete=models.CASCADE)
    prisoner=models.ForeignKey(Prisonerprofile,null=True, blank=True, on_delete=models.CASCADE)
    visitationdate=models.DateTimeField(max_length=40,null=True)
    
    phoneNo=models.CharField(max_length=13,null=True, unique=True)
   
    status=models.CharField(max_length=40,null=True,blank=True,default="Pending")
    Prisonernumber=models.IntegerField(blank=True,null=True)
    date=models.DateTimeField(auto_now=True,max_length=40,null=True)


    def __str__(self):
        return self.status or None