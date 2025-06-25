from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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
    
    # Serialize and return the file data
    serializer = FileSerializer(file_obj)
    return Response(serializer.data, status=status.HTTP_200_OK)
