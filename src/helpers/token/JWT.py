import json 
import datetime
import jwt

def generate(obj):

    encoded = jwt.encode({
        "value": obj,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, "SECRET_KEY", algorithm="HS256")

    return encoded

def decode(token):

    decoded = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])

    return decoded