import falcon

class CatController(object):

    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.text = "working"