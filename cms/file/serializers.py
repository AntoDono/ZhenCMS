from rest_framework import serializers
from .models import File
from folder.models import Folder


class FolderSerializer(serializers.ModelSerializer):
    """Simple folder serializer for nested representation"""
    class Meta:
        model = Folder
        fields = ['id', 'name']


class FileSerializer(serializers.ModelSerializer):
    """Comprehensive File serializer with all fields and computed properties"""
    
    # Read-only computed properties
    file_extension = serializers.ReadOnlyField()
    is_image = serializers.ReadOnlyField()
    is_document = serializers.ReadOnlyField()
    formatted_size = serializers.ReadOnlyField()
    file_url = serializers.SerializerMethodField()
    folder_path = serializers.SerializerMethodField()
    
    # Nested folder representations
    folder = FolderSerializer(read_only=True)
    root_folder = FolderSerializer(read_only=True)
    
    class Meta:
        model = File
        fields = [
            'id',
            'uuid',
            'name',
            'original_filename',
            'uploaded_at',
            'size_in_bytes',
            'formatted_size',
            'content_type',
            'file_extension',
            'is_image',
            'is_document',
            'file_url',
            'folder_path',
            'folder',
            'root_folder',
            'shareable',
        ]
        read_only_fields = [
            'id',
            'uuid',
            'uploaded_at',
            'size_in_bytes',
            'original_filename',
        ]
    
    def get_file_url(self, obj):
        """Get the file URL"""
        return obj.get_file_url()
    
    def get_folder_path(self, obj):
        """Get the full folder path"""
        return obj.get_folder_path() 