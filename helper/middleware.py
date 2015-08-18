import json
from django.http import HttpResponse
from helper.exceptions import HtmlViewerWebException


class LocaleMiddleware(object):

    @staticmethod
    def process_exception(request, exception):
        if type(exception) is HtmlViewerWebException:
            return HttpResponse(json.dumps({"message": exception.message}), status=exception.status)