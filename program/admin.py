from django.contrib import admin

from  embed_video.admin  import  AdminVideoMixin
from .models import *

# Register your models here.

@admin.register(Program)
class ProgramAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display_links = ('title',)
    search_fields = ('title',)
    list_display = ("title",)
    prepopulated_fields = {'slug': ('title',)}
    pass



admin.site.register(ProgramNum)
