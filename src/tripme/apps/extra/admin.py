from django.contrib import admin
from extra.models import Quote

# -------------------------------------------------------- #
# quotes
# -------------------------------------------------------- #
admin.site.register(Quote,
    ordering      = ["author"],
    search_fields = ["author","quote"],
    list_display  = ["author","quote"],
    list_filter   = ["author"],
    prepopulated_fields = {'slug': ('author', 'quote',)},
    list_per_page = 200,
)
