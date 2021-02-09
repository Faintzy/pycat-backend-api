import falcon
import json
from pony.orm.core import commit
from models.db import User
from helpers.validate import validateRequest
from helpers.token import JWT

class UserController(object):

    def on_put(self, req, response):

        reqBody = json.dumps(req.media)
        reqObj = json.loads(reqBody)
        validate = validateRequest(reqObj)

        if validate.get('result') == False:

            response.status = falcon.HTTP_401

            response.text = json.dumps({
                "success": False,
                "content": validate.get('errors')
            })
        
        else:

            User.create(username=reqObj['username'], password=reqObj['password'])

            response.status = falcon.HTTP_200

            response.text = json.dumps({
                "success": False,
                "content": "User created successful"
            })

    def on_post(self, req, response):

        reqObj = req.media

        usr = User.auth(username=reqObj['username'], password=reqObj['password'])

        if usr != '0':

            response.status = falcon.HTTP_200
            response.text = json.dumps({
                "success": True,
                "content": str(JWT.generate([usr]))
            })

        else: 

            response.status = falcon.HTTP_401
            response.text = json.dumps({
                "success": False,
                "content": "Incorrect credentials"
            })

    def on_get(self, req, response):

        response.status = falcon.HTTP_200
        response.text = "Only for authenticated users"