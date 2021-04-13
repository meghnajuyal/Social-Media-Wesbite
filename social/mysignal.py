from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from social.models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def save(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,name=instance.username)
