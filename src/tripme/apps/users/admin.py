from django.contrib import admin
from apps.users.models import *
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = UserProfile

admin.site.unregister(User)
admin.site.register(User,
    inlines         = [UserProfileInline]
)

admin.site.register(Service,
    ordering      = ["profile"],
    search_fields = ["profile"],
    list_display  = ["profile","service"],
    list_filter   = ["profile","service"],
    list_per_page = 200,
)

admin.site.register(ServiceType)
