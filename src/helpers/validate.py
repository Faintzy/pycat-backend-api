from falcon import request
from validator import validate

def validateRequest(obj):

    rules = {
        "username": "required|min:4|max:60",
        "password": "required|min:6"
    }

    result, _, errors = validate(obj, rules, return_info=True)

    return {
        "result": result,
        "errors": errors
    } 