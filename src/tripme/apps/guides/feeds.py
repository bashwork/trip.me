from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf.urls.defaults import *
from guides.models import *

# -------------------------------------------------------- #
# guide feed generators
# -------------------------------------------------------- #
class LatestGuidesFeed(Feed):
    title = "Trip.me Newest Guides"
    link  = "/guides/"
    description = "Updates on the latest created guides on trip.me"

    def items(self):
        ''' Returns a collection of the latest guides

        :returns: A collection of the latest guides
        '''
        return Guide.objects.order_by('-created')[:5]

    def item_title(self, item):
        ''' Returns the title of the guide

        :returns: The title of the specified guide
        '''
        return item.name

    def item_description(self, item):
        ''' Returns a description of the guide

        :returns: A description of the given guide
        '''
        return item.description

class LatestGuidesAtomFeed(LatestGuidesFeed):
    feed_type = Atom1Feed
    subtitle = LatestGuidesFeed.description

# -------------------------------------------------------- #
# guide feed urls
# -------------------------------------------------------- #
urlpatterns = patterns('',
    (r'^rss/', LatestGuidesFeed()),
    (r'^atom/', LatestGuidesAtomFeed()),
)
