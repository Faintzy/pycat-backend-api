import falcon 
import json
from helpers.token import JWT
from routes.page.pageRouter import pageRoutes

class AuthMiddleware(object):

    def process_request(self, req, resp):

        blacklist = []

        for key, val in pageRoutes.items():

            blacklist.append(key)

        if req.path in blacklist:

            token = req.get_header('Authorization')

            if token is None:

                resp.status = falcon.HTTP_401
                resp.text = json.dumps({
                    "success": False,
                    "content": "JWT required"
                })
            
            try:
                decoded = JWT.decode(token)
            except:
                raise falcon.HTTPForbidden(title="Not Authenticated", description="Please login")