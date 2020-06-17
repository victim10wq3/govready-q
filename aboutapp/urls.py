from django.conf.urls import include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from . import views
from siteapp.settings import *

urlpatterns = [
    url(r'^test$', views.test),

    url(r'^$', views.about),
    url(r'^changelog$', views.changelog),
    # url(r'^catalogs/(?P<catalog_key>.*)/$', views.catalog),

]
