import logging
from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from guides.models import UserProfile

logger = logging.getLogger(__name__)

@reciever(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    '''
    This is used to make sure a user profile is created
    when we create an initial user
    '''
    profile, new = UserProfile.objects.get_or_create(user=instance)
    if new is not None:
        logger.debug("created user[%s] profile" % instance)

