from django.contrib import admin
from .models import Listing


# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'branch', 'price', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('branch',)
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'category', 'price')
    list_per_page = 30


admin.site.register(Listing, ListAdmin)
