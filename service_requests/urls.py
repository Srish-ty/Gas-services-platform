from django.urls import path
from .views import ServiceRequestListView, ServiceRequestCreateView

urlpatterns = [
    path('', ServiceRequestListView.as_view(), name='request_list'),
    path('new/', ServiceRequestCreateView.as_view(), name='request_create'),
]
