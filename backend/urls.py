from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
url(r'add_layman$', views.add_layman, ),
url(r'query',views.query, ),
]