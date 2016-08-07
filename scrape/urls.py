from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.baseSite, name='baseSite'),
    url(r'runScraper$', views.newSite, name='newSite'),
    ]
