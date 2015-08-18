from django.conf.urls import patterns, url
from helper.views import test

urlpatterns = patterns('',
                       url(r'', test),
)
