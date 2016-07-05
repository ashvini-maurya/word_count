from django.conf.urls import patterns, url
from count import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^getValue/', views.getValue, name="index"),
                       )
