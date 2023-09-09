from django.urls import path
from .views import MyDataAPIView

urlpatterns = [
    path('api/', MyDataAPIView.as_view(), name='my-data-api'),
]
