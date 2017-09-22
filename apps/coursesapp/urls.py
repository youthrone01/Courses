from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^destroy/(?P<course_id>[0-9]+)$', views.destroy),
    url(r'^comment/(?P<course_id>[0-9]+)$', views.comment),
    
]