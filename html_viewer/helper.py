from html.parser import HTMLParser
import urllib
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_502_BAD_GATEWAY
from helper.exceptions import HtmlViewerWebException


def validate_url(url):
    val = URLValidator()
    try:
        val(url)
    except ValidationError:
        raise HtmlViewerWebException("Enter a valid url. Eg: http://slack.com, http://www.slack.com",
                                     HTTP_400_BAD_REQUEST)
    try:
        uf = urllib.request.urlopen(url)
    except:
        raise HtmlViewerWebException("Url not reachable", HTTP_502_BAD_GATEWAY)
    try:
        html_source = uf.read().decode('utf-8')
    except:
        raise HtmlViewerWebException("Unreadable data format. Might not be text", HTTP_400_BAD_REQUEST)
    return html_source, uf


class HTMLTagParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_count_summary = {}
        self.tag_position_summary = {}

    def handle_starttag(self, tag, attrs):
        ("Encountered a start tag:" + tag + " " + str(self.getpos()))
        if tag in self.tag_count_summary:
            self.tag_count_summary[tag] += 1
        else:
            self.tag_count_summary[tag] = 1
        self.tag_position_summary[str(self.getpos()[0])] = (tag, self.getpos()[1])

    def handle_endtag(self, tag):
        self.tag_position_summary[str(self.getpos()[0])] = (tag, self.getpos()[1])
        print("Encountered an end tag :", tag)