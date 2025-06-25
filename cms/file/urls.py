from django.urls import path
from . import views

app_name = 'file'

urlpatterns = [
    path('api/get-by-uuid/', views.get_file_by_uuid, name='get_file_by_uuid'),
    path('download/<uuid:uuid>/', views.download_file_by_uuid, name='download_file_by_uuid'),
] 