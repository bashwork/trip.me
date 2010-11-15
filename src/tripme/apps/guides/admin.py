from guides.models import *
from django.contrib import admin

# -------------------------------------------------------- #
# World Locations
# -------------------------------------------------------- #
admin.site.register(Country,
    alphabet_filter = "name",
    ordering      = ["name"],
    search_fields = ["name","code"],
    list_display  = ["name","code","capital"],
    list_filter   = [],
    list_per_page = 200,
)
admin.site.register(Region,
    alphabet_filter = "name",
    ordering      = ["name"],
    search_fields = ["name","code"],
    list_display  = ["name","code","country"],
    list_filter   = [],
    list_per_page = 200,
)
admin.site.register(City,
    alphabet_filter = "name",
    ordering      = ["name"],
    search_fields = ["name","code"],
    list_display  = ["name","code","region","timezone","latitude","longitude"],
    list_filter   = [],
    raw_id_fields = ["region"],
    list_per_page = 200,
)
admin.site.register(Spot,
    alphabet_filter = "name",
    ordering      = ["name"],
    search_fields = ["name","zipcode"],
    list_display  = ["name","city","address","zipcode","latitude","longitude"],
    list_filter   = [],
    raw_id_fields = ["city"],
    list_per_page = 200,
)

# -------------------------------------------------------- #
# User Guides
# -------------------------------------------------------- #
class GuideLocationEntryInline(admin.StackedInline):
    model = GuideLocationEntry
    raw_id_fields = ["city"]
    extra = 3

admin.site.register(Guide,
    alphabet_filter = "name",
    ordering        = ["modified"],
    search_fields   = ["name","user"],
    list_display    = ["name","user","created","modified"],
    list_filter     = ["modified"],
    list_per_page   = 500,
    inlines         = [GuideLocationEntryInline]
)
