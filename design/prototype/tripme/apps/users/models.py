from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------------- #
# user profile extension
# -------------------------------------------------------- #
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    image = models.ImageField(upload_to="users/%Y/%m", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #first_time = models.BooleanField(default=True)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    flickr = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.user

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

