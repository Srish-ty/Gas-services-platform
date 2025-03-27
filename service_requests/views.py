from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import ServiceRequest
from .forms import ServiceRequestForm

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
