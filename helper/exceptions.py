
class HtmlViewerWebException(Exception):
    def __init__(self, message, status):
        super(HtmlViewerWebException, self).__init__(message)
        self.status = status
        self.message = message