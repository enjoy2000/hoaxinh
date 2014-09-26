from django.db import models
from django.contrib.auth.models import User
from awesome_avatar.fields import AvatarField
from django.db.models.signals import post_save

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^awesome_avatar\.fields\.AvatarField"])
except:
    pass

GENDER_CHOICES = (
                  (True, 'Male'),
                  (False, 'Female'),
                  )

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullname = models.CharField(max_length=255, blank=True, default='')
    avatar = AvatarField(upload_to='avatars', width=200, height=200)
    homepage = models.URLField(default='', blank=True)
    gender = models.BooleanField(default=True, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True, null=True, default=None)

    def __unicode__(self):
        return 'Profile for user %s' % self.user_id

from django import dispatch

@dispatch.receiver(post_save, sender=User)
def create_book_profile(sender, **kwargs):
    if kwargs.get('created'):
        user = kwargs.get('instance')
        profile = UserProfile(user=user)
        profile.save()
