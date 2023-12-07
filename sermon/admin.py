from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources  
from import_export.admin import ImportExportMixin

from .models import *

# Register your models here


class SermonResource(resources.ModelResource):
    class Meta:
        model = Sermon
        fields = ('author', 'title', 'created', 'id',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ("name","created", "updated")
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



@admin.register(Sermon)
class SermonAdmin(DjangoQLSearchMixin, ImportExportMixin, admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ("author","title", "created", "updated")
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('author', 'title',)
    resource_classes = (SermonResource,)

