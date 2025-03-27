from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import ServiceRequest
from .forms import ServiceRequestForm

# View for listing requests
class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)

# View for creating a new request
class ServiceRequestCreateView(CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/request_form.html'
    success_url = reverse_lazy('request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
