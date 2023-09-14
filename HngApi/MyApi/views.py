from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        persons = self.get_queryset()
        serializer = self.get_serializer(persons, many=True)
        
        data = {
            "message": "List of all persons retrieved successfully.",
            "data": serializer.data,
        }
        
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Person created successfully.",
                "data": serializer.data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message": "Failed to create person.",
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

            

class PersonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        data = {
            "message": "Person retrieved successfully.",
            "data": serializer.data,
        }
        
        return Response(data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Person updated successfully.",
                "data": serializer.data,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "message": "Failed to update person.",
                "errors": serializer.errors,
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        data = {
            "message": "Person deleted successfully.",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

