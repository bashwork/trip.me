def aggregator_conext(request):
    from django.contrib.sites.models import Site

    return {
        'site': Site.objects.get_current(),
    }
