import falcon
from falcon.status_codes import HTTP_200

class PageController(object):

    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.text = 'you can see'