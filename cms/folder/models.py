from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    root = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='descendants')
    
    def __str__(self):
        return self.name  