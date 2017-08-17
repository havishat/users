from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'show/(?P<id>\d+)$', views.show),
    url(r'new', views.new),
    url(r'edit/(?P<id>\d+)$', views.edit),
    url(r'delete/(?P<id>\d+)$', views.delete), 
    url(r'create$', views.create),
    url(r'update/(?P<id>\d+)$', views.update),
]