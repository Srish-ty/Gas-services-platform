from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from .forms import ServiceRequestForm, SignupForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('request_list')  # Redirect to service requests
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/request_form.html'
    success_url = reverse_lazy('request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ServiceRequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ServiceRequest
    fields = ['status']
    template_name = 'service_requests/request_update.html'
    success_url = reverse_lazy('request_list')

    def test_func(self):
        # to allow only staff users to update the status
        return self.request.user.is_staff


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('request_list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

class ServiceRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ServiceRequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]