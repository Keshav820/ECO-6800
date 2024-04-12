from bottle import HTTPResponse
from multipledispatch import dispatch
from classes.exceptions import BadAuthException

import json

@dispatch(ValueError)
def handler(e: ValueError):
    return HTTPResponse(
            body=json.dumps({'error': str(e)}),
            status=400,
            headers={'Content-Type': 'application/json'}
        )
@dispatch(TypeError)
def handler(e: TypeError):
    return HTTPResponse(
            body=json.dumps({'error': str(e)}),
            status=400,
            headers={'Content-Type': 'application/json'}
        )
@dispatch(BadAuthException)
def handler(e: BadAuthException):
    return HTTPResponse(
            body=json.dumps({'error': str(e)}),
            status=403,
            headers={'Content-Type': 'application/json'}
        )