"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

import backend.urls

from backend import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include(backend.urls)),
    url(r'^$',TemplateView.as_view(template_name="recruit.html")),
    url(r'^arrangement',TemplateView.as_view(template_name = "arrangement.html")),
    url(r'^result',TemplateView.as_view(template_name = "result.html")),
    url(r'^recruit_north',TemplateView.as_view(template_name='recruit_north.html')),

    url(r'^computer_clinic',TemplateView.as_view(template_name = "computer_clinic.html")),
    url(r'export_cc',views.export_csv_cc),
]