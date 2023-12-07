from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(WeekService)
class WeekServiceAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    search_fields = ('name',)
    list_display = ("name","time", "created", "updated")
    prepopulated_fields = {'slug': ('name',)}


admin.site.register([Mfm, Contact])