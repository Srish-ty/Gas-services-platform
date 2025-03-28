from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ServiceRequestListView, ServiceRequestCreateView, ServiceRequestUpdateView, signup_view, ServiceRequestListCreateAPIView, ServiceRequestDetailAPIView

urlpatterns = [
    path('', ServiceRequestListView.as_view(), name='request_list'),
    path('new/', ServiceRequestCreateView.as_view(), name='request_create'),
    path('<int:pk>/update/', ServiceRequestUpdateView.as_view(), name='request_update'),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/requests/', ServiceRequestListCreateAPIView.as_view(), name='api_request_list'),
    path('api/requests/<int:pk>/', ServiceRequestDetailAPIView.as_view(), name='api_request_detail'),
]
