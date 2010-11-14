from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------------- #
# choices
# -------------------------------------------------------- #
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# -------------------------------------------------------- #
# user profile extension
# -------------------------------------------------------- #
class UserProfile(models.Model):
    '''
    This is an extension to the django user model to add
    extra profile information for the specified user. It
    is linked to the following models:

    * :model:`auth.User`
    '''
    user = models.ForeignKey(User, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to="img/users/%Y/%m", null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.user.get_full_name()

    @models.permalink
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })

class ServiceType(models.Model):
    '''
    This defines a type of social networking service that a
    user can link their profile to. Examples include twitter,
    facebook, flickr, etc.
    '''
    title = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to="icons/", null=True, blank=True)
    url = models.URLField(blank=True, verify_exists=False,
        help_text='URL with a single \'{user}\' placeholder to turn a username into a service URL')

    def __unicode__(self):
        return "%s" % self.title

class Service(models.Model):
    '''
    This is an instance of a given social networking service
    that a user has linked to. This is connected to the
    following tables:

    * :model:`users.UserProfile`
    * :model:`users.ServiceType`
    '''
    service = models.ForeignKey(ServiceType)
    profile = models.ForeignKey(UserProfile)
    username = models.CharField(max_length=100,
        help_text="Username or id to be inserted into the service url")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.username

    @property
    def service_url(self):
        return re.sub('{user}', self.username, self.service.url)

    @property
    def title(self):
        return u"%s" % self.service.title
