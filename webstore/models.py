from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(User=kwargs['instance'])


post_save.connect(create_profile, sender=User)
