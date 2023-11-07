from django.contrib import admin

from .models import *
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data']
    list_display_links = ('id', 'title')
    search_fields = ('title', 'place', 'description')
    list_filter = ('is_done', 'place')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event, EventAdmin)