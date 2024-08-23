from django.urls import path
from .views import (
    CourseListCreateView,
    CourseDetailView,
    CourseInstanceListCreateView,
    CourseInstanceDetailView,
    CourseInstanceInfoView,
)

urlpatterns = [
    path('api/courses', CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>', CourseDetailView.as_view(), name='course-detail-delete'),
    path('api/instances', CourseInstanceListCreateView.as_view(), name='instance-list-create'),
    path('api/instances/<int:year>/<int:semester>', CourseInstanceDetailView.as_view(), name='instance-detail'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>', CourseInstanceInfoView.as_view(), name='instance-info'),
]
