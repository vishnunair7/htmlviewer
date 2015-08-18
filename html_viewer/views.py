import html
import json

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from helper.exceptions import HtmlViewerWebException

from html_viewer.helper import validate_url, HTMLTagParser
from html_viewer.models import UrlContentStore

POSITION_URL = "position_url"

COUNT_URL = "count_url"

POSITION = "position"

COUNT = "count"

UUID = 'uuid'

CONTENT = 'content'

SOURCE_URL = "http://107.170.231.146/api/source/"


# Validates the url and returns content. Also parses the html and creates the tag count and position summary
@csrf_exempt
@api_view(['GET'])
def get_url_content(request):
    url = request.GET.get('url')
    html_source, uf = validate_url(url)

    soup = BeautifulSoup(html_source)
    html_source = soup.prettify()
    uf.close()
    parser = HTMLTagParser()
    parser.feed(html_source)
    url_content = UrlContentStore()
    url_content.content = html_source
    url_content.tag_count_summary = parser.tag_count_summary
    url_content.tag_position_summary = parser.tag_position_summary
    url_content.save()
    count_url = SOURCE_URL + str(url_content.id) + "/" + COUNT
    position_url = SOURCE_URL + str(url_content.id) + "/" + POSITION
    response_dict = {CONTENT: html.escape(html_source), UUID: str(url_content.id), COUNT_URL: count_url, POSITION_URL: position_url}
    return HttpResponse(json.dumps(response_dict), content_type="application/json")


@csrf_exempt
@api_view(['GET'])
def get_count_summary(request, source_uuid):
    url_content = UrlContentStore.objects(id=source_uuid).first()
    if url_content is None:
        raise HtmlViewerWebException("Invalid url reference",
                                     HTTP_400_BAD_REQUEST)
    summary_result_dict = {COUNT: url_content.tag_count_summary}
    return HttpResponse(json.dumps(summary_result_dict), content_type="application/json")


@csrf_exempt
@api_view(['GET'])
def get_position_summary(request, source_uuid):
    url_content = UrlContentStore.objects(id=source_uuid).first()
    if url_content is None:
        raise HtmlViewerWebException("Invalid url reference",
                                     HTTP_400_BAD_REQUEST)
    summary_result_dict = {POSITION: url_content.tag_position_summary}
    return HttpResponse(json.dumps(summary_result_dict), content_type="application/json")


