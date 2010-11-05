from guides.models import *
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
admin.site.register(Guide,
    ordering      = ["name"],
    search_fields = ["name","user","pub_date"],
    list_display  = ["name","user","pub_date"],
    list_filter   = ["name","pub_date"],
    list_per_page = 500,
)
