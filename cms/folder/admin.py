from django.contrib import admin
from .models import Folder

# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'root']
    list_filter = ['parent', 'root']
    search_fields = ['name']
