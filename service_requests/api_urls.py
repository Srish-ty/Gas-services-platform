from django.urls import path
from .views import ServiceRequestListCreateAPIView, ServiceRequestDetailAPIView

urlpatterns = [
    path('requests/', ServiceRequestListCreateAPIView.as_view(), name='api_request_list'),
    path('requests/<int:pk>/', ServiceRequestDetailAPIView.as_view(), name='api_request_detail'),
]
