from django.conf.urls import url, include
#from django.urls import path
from . import views

urlpatterns = [
url(r'add_layman$', views.add_layman, ),
url(r'query',views.query, ),
url(r'add_layman_north',views.add_layman_north ),
url(r'cc',views.cc ),
url(r'export_msc',views.export_csv_msc),

#url(r'export_cc',views.export_csv_cc),
]