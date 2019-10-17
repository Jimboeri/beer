from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
#from django.core.validators import MinValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=50, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Registration(models.Model):
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Competition(models.Model):
    descr = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    compdate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.descr