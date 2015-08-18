from django.conf.urls import patterns, url
from html_viewer.views import get_url_content, get_count_summary, get_position_summary

urlpatterns = patterns('',
                       url(r'/source$', get_url_content),
                       url(r'/source/(?P<source_uuid>\w+)/count', get_count_summary),
                       url(r'/source/(?P<source_uuid>\w+)/position', get_position_summary),
)
