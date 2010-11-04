from guides.models import City,Spot
from django.contrib import admin

admin.site.register(City,
    ordering      = ["name"],
    search_fields = ["name","country","state"],
    list_display  = ["name","country","state"],
    list_filter   = ["name"],
    list_per_page = 500,
)
admin.site.register(Spot,
    ordering      = ["name"],
    search_fields = ["name","address"],
    list_display  = ["name","address"],
    list_filter   = ["name"],
    list_per_page = 500,
)
