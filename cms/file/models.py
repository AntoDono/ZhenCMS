from django.db import models
from django.core.files.storage import default_storage
from folder.models import Folder
from uuid import uuid4
import os

# Create your models here.
def file_upload_path(instance, filename):
    """Generate upload path based on folder structure and UUID"""
    # Use UUID to avoid filename conflicts
    ext = os.path.splitext(filename)[1]
    filename = f"{instance.uuid}{ext}"
    
    # Create path based on folder hierarchy
    folder_path = instance.get_folder_path()
    return os.path.join('files', folder_path, filename)

class File(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size_in_bytes = models.BigIntegerField(default=0)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    root_folder = models.ForeignKey(Folder, related_name='all_files', on_delete=models.CASCADE, null=True, blank=True)
    # New fields for actual file storage
    file = models.FileField(upload_to=file_upload_path, null=True, blank=True)
    content_type = models.CharField(max_length=255, blank=True)
    original_filename = models.CharField(max_length=255, blank=True)
    
    # Sharing control
    shareable = models.BooleanField(default=False, help_text="Whether this file can be accessed via API")
    
    # View tracking
    views = models.PositiveIntegerField(default=0, help_text="Number of times this file has been viewed")
    
    def save(self, *args, **kwargs):
        # Auto-populate fields when file is uploaded
        if self.file:
            self.size_in_bytes = self.file.size
            self.original_filename = self.file.name
            # Set name to original filename if not provided
            if not self.name:
                self.name = os.path.basename(self.file.name)
        super().save(*args, **kwargs)
    
    def get_folder_path(self):
        """Get the full folder path for file organization"""
        if not self.folder:
            return ''
        
        path_parts = []
        current_folder = self.folder
        
        # Build path from current folder to root
        while current_folder:
            path_parts.append(current_folder.name)
            current_folder = current_folder.parent
        
        # Reverse to get root-to-current order
        path_parts.reverse()
        return '/'.join(path_parts)
    
    def get_file_url(self):
        """Get the URL to access the file"""
        if self.file:
            return self.file.url
        return None
    
    def get_file_path(self):
        """Get the file system path of the file"""
        if self.file:
            return self.file.path
        return None
    
    def read_file(self):
        """Read and return file content"""
        if self.file:
            try:
                with self.file.open('rb') as f:
                    return f.read()
            except Exception as e:
                return None
        return None
    
    def delete_file(self):
        """Delete the actual file from storage"""
        if self.file:
            if default_storage.exists(self.file.name):
                default_storage.delete(self.file.name)
    
    def delete(self, *args, **kwargs):
        """Override delete to also remove file from storage"""
        self.delete_file()
        super().delete(*args, **kwargs)
    
    def increment_views(self):
        """Increment the view count for this file"""
        self.views += 1
        self.save(update_fields=['views'])
    
    @property
    def file_extension(self):
        """Get file extension"""
        if self.original_filename:
            return os.path.splitext(self.original_filename)[1].lower()
        elif self.file:
            return os.path.splitext(self.file.name)[1].lower()
        return ''
    
    @property
    def is_image(self):
        """Check if file is an image"""
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']
        return self.file_extension in image_extensions
    
    @property
    def is_document(self):
        """Check if file is a document"""
        doc_extensions = ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt']
        return self.file_extension in doc_extensions
    
    @property
    def formatted_size(self):
        """Return human-readable file size"""
        size = self.size_in_bytes
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} PB"
    
    def __str__(self):
        return self.name