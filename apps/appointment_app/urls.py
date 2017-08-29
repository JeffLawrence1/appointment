from django.conf.urls import url, include
from django.contrib import admin
from . import views

# def test(request):
#     print "***appointment_app urls***"


urlpatterns = [
    # url(r'^', test),
    # url(r'^$', views.test),
    url(r'^$', views.index),
    url(r'^/updatep/(?P<id>\d+)$', views.updatep), 
    # url(r'^/uperror$', views.uperror), 
    url(r'^/add$', views.addtask),
    url(r'^/update/(?P<id>\d+)$', views.update, name="update"), 
    url(r'^/remove/(?P<id>\d+)$', views.remove), 
]
