from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from python_test import views


clients_urlpatterns = [
    path('', views.ClientsIndexView.as_view(), name='index'),
    path('create/', views.ClientCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.ClientEditView.as_view(), name='edit'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),

    path('clients/', include((clients_urlpatterns, 'clients')))
]
