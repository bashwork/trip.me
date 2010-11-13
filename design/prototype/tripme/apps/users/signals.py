import logging
from django.db.models import signals
from django.contrib.auth.models import User
from apps.users.models import UserProfile

logger = logging.getLogger(__name__)

def user_post_save(sender, instance, **kwargs):
    '''
    This is used to make sure a user profile is created
    when we create an initial user
    '''
    logger.debug("received user[%s] created signal" % instance)
    profile, new = UserProfile.objects.get_or_create(user=instance)
    if new is not None:
        logger.debug("created user[%s] profile" % instance)

signals.post_save.connect(user_post_save, sender=User)
