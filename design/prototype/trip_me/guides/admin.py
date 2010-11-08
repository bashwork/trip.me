from guides.models import *
from django.contrib import admin

# -------------------------------------------------------- #
# World Locations
# -------------------------------------------------------- #
admin.site.register(Country,
    ordering      = ["name"],
    search_fields = ["name","code"],
    list_display  = ["name","code","capital"],
    list_filter   = ["name",],
    list_per_page = 500,
)
admin.site.register(Region,
    ordering      = ["name"],
    search_fields = ["name","code"],
    list_display  = ["name","code","country"],
    list_filter   = ["name","country"],
    list_per_page = 500,
)
admin.site.register(City,
    ordering      = ["name"],
    search_fields = ["name","code","country","region"],
    list_display  = ["name","code","country","region","timezone","latitude","longitude"],
    list_filter   = ["name","country","region"],
    list_per_page = 500,
)
admin.site.register(Spot,
    ordering      = ["name"],
    search_fields = ["name","city","zipcode"],
    list_display  = ["name","city","address","zipcode","latitude","longitude"],
    list_filter   = ["name","city"],
    list_per_page = 500,
)

# -------------------------------------------------------- #
# User Guides
# -------------------------------------------------------- #
admin.site.register(Guide,
    ordering      = ["name"],
    search_fields = ["name","user","pub_date"],
    list_display  = ["name","user","pub_date"],
    list_filter   = ["name","pub_date"],
    list_per_page = 500,
)
