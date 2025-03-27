from django.urls import path
from .views import ServiceRequestListView, ServiceRequestCreateView, ServiceRequestUpdateView

urlpatterns = [
    path('', ServiceRequestListView.as_view(), name='request_list'),
    path('new/', ServiceRequestCreateView.as_view(), name='request_create'),
    path('<int:pk>/update/', ServiceRequestUpdateView.as_view(), name='request_update'),
]
