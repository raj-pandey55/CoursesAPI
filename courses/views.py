from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course Views

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# CourseInstance Views

class CourseInstanceListCreateView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

class CourseInstanceDetailView(APIView):
    def get(self, request, year, semester):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(instances, many=True)
        return Response(serializer.data)

class CourseInstanceInfoView(APIView):
    def get(self, request, year, semester, pk):
        try:
            instance = CourseInstance.objects.get(year=year, semester=semester, pk=pk)
            serializer = CourseInstanceSerializer(instance)
            return Response(serializer.data)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, year, semester, pk):
        try:
            instance = CourseInstance.objects.get(year=year, semester=semester, pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
