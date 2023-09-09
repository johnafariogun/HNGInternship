from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MyDataSerializer

class MyDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        slack_name = self.request.query_params.get('slack_name', '')
        track = self.request.query_params.get('track', 'Unknown')
        
        current_day = timezone.now().strftime('%A')
        utc_time = timezone.now()
        
        data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': 'https://github.com/johnafariogun/HNGInternship/blob/main/HngApi/MyApi/apps.py',
            'github_repo_url': 'https://github.com/johnafariogun/HNGInternship',
            'status_code': 200,
        }
        
        serializer = MyDataSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
