from django.contrib import admin
from .models import File

# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'folder', 'formatted_size', 'content_type', 'uploaded_at', 'file_extension', 'views', 'shareable']
    list_filter = ['uploaded_at', 'content_type', 'folder', 'shareable']
    search_fields = ['name', 'original_filename', 'content_type']
    readonly_fields = ['uploaded_at', 'size_in_bytes', 'original_filename', 'file_extension', 'formatted_size', 'views']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'folder', 'root_folder')
        }),
        ('File Data', {
            'fields': ('file', 'content_type')
        }),
        ('Access Control', {
            'fields': ('shareable',)
        }),
        ('Metadata', {
            'fields': ('uuid', 'uploaded_at', 'size_in_bytes', 'formatted_size', 'original_filename', 'file_extension', 'views'),
            'classes': ('collapse',)
        })
    )
