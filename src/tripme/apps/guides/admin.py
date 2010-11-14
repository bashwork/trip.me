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
    list_display  = ["name","code","country","region","timezone","latitude","longitude"],
    list_filter   = [],
    list_per_page = 200,
)
admin.site.register(Spot,
    alphabet_filter = "name",
    ordering      = ["name"],
    search_fields = ["name","zipcode"],
    list_display  = ["name","city","address","zipcode","latitude","longitude"],
    list_filter   = [],
    list_per_page = 200,
)

# -------------------------------------------------------- #
# User Guides
# -------------------------------------------------------- #
admin.site.register(Guide,
    alphabet_filter = "name",
    ordering      = ["modified"],
    search_fields = ["name","user"],
    list_display  = ["name","user","created","modified"],
    list_filter   = ["modified"],
    list_per_page = 500,
)
