from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels$', views.index),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^addTrip$', views.addTrip),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^join/(?P<id>\d+)$', views.join),
]