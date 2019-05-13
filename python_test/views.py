from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from python_test import models, filters


class SuccessMessageMixin:
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message.format(cleaned_data)


class ClientsIndexView(FilterView):
    model = models.Client
    queryset = model.objects.order_by('name')
    filterset_class = filters.ClientFilter
    template_name = 'list.html'
    context_object_name = 'clients'
    paginate_by = 20


class ClientCreateView(SuccessMessageMixin,
                       generic.CreateView):
    model = models.Client
    template_name = 'form.html'
    fields = [
        'name',
        'street_name',
        'suburb',
        'postcode',
        'state',
        'contact_name',
        'email',
        'phone_number',
    ]
    success_url = reverse_lazy('clients:index')
    success_message = 'Client object has been created!'


class ClientEditView(SuccessMessageMixin,
                     generic.UpdateView):
    model = models.Client
    template_name = 'form.html'
    fields = [
        'name',
        'street_name',
        'suburb',
        'postcode',
        'state',
        'contact_name',
        'email',
        'phone_number',
    ]
    success_url = reverse_lazy('clients:index')
    success_message = 'Client object has been updated!'
