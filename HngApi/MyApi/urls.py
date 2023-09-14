from django.urls import path
from .views import PersonListCreateView, PersonDetailView
# from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Simple HNG API",
      default_version='v1.',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="afariogun.john2002@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
