from django.conf.urls import url
from django.contrib import admin
from features.views import ClientApiView, ClientDetailApiView, FeatureApiView, FeatureDetailApiView

urlpatterns = [
    url(r'^clients/$', ClientApiView.as_view()),
    url(r'^client/(?P<pk>\d+)/$', ClientDetailApiView.as_view()),
    url(r'^features/$', FeatureApiView.as_view()),
    url(r'^feature/(?P<pk>\d+)/$', FeatureDetailApiView.as_view()),
]
