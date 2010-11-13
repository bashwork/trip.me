from django.contrib import admin
from apps.users.models import *

admin.site.register(UserProfile,
    alphabet_filter = "user",
    ordering      = ["user"],
    search_fields = ["user"],
    list_display  = ["user"],
    list_filter   = [],
    list_per_page = 200,
)

admin.site.register(Service,
    ordering      = ["profile"],
    search_fields = ["profile"],
    list_display  = ["profile","service"],
    list_filter   = ["profile","service"],
    list_per_page = 200,
)

admin.site.register(ServiceType)
