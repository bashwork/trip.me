from django.conf import settings
from django.contrib.sites.models import Site

def global_settings(request):
    return {
        'settings': settings,
        'site': Site.objects.get_current(),
    }
