from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
from .models import File
from .serializers import FileSerializer

# Create your views here.

@api_view(['POST'])
def get_file_by_uuid(request):
    """
    POST endpoint to retrieve file data by UUID
    
    Expected request body:
    {
        "uuid": "file-uuid-here"
    }
    
    Returns:
    - 200: File data in JSON format
    - 400: Bad request (missing or invalid UUID)
    - 403: File exists but is not shareable
    - 404: File not found
    """
    
    # Get UUID from request data
    uuid = request.data.get('uuid')
    
    if not uuid:
        return Response(
            {'error': 'UUID is required in request body'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Try to get the file by UUID with 404 handling
    try:
        file_obj = get_object_or_404(File, uuid=uuid)
    except Exception:
        return Response(
            {'error': 'File not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Check if file is shareable
    if not file_obj.shareable:
        return Response(
            {'error': 'File is not shareable'}, 
            status=status.HTTP_403_FORBIDDEN
        )
    
    # Increment view count
    file_obj.increment_views()
    
    # Serialize and return the file data
    serializer = FileSerializer(file_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
def download_file_by_uuid(request, uuid):
    """
    GET endpoint to download file by UUID
    
    Returns:
    - 200: File download with proper headers
    - 403: File exists but is not shareable
    - 404: File not found
    """
    
    # Try to get the file by UUID
    try:
        file_obj = get_object_or_404(File, uuid=uuid)
    except Exception:
        raise Http404("File not found")
    
    # Check if file is shareable
    if not file_obj.shareable:
        raise Http404("File not found")
    
    # Check if file exists on disk
    if not file_obj.file or not os.path.exists(file_obj.get_file_path()):
        raise Http404("File not found on disk")
    
    # Prepare the response with proper headers for download
    try:
        with open(file_obj.get_file_path(), 'rb') as f:
            # Use the original content type if available, fallback to octet-stream
            content_type = file_obj.content_type if file_obj.content_type else 'application/octet-stream'
            response = HttpResponse(f.read(), content_type=content_type)
            
        # Set headers to force download
        filename = f"{file_obj.name}{file_obj.file_extension}"
        # Use both attachment and inline to support different browsers/devices
        response['Content-Disposition'] = f'attachment; filename="{filename}"; filename*=UTF-8\'\'{filename}'
        response['Content-Length'] = file_obj.size_in_bytes
        
        # Add CORS headers to allow cross-origin downloads
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Content-Disposition'
        response['Access-Control-Expose-Headers'] = 'Content-Disposition, Content-Length'
        
        # Additional headers for better mobile compatibility
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
        
    except Exception as e:
        raise Http404("Error reading file")
