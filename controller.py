from bottle import Bottle, request, response, run, HTTPResponse
from classes.request import CreateEventRequest

from classes.response import CreateEventResponse

from service import auth_service
from service import exception_handler
from service import event_service

import json

def startup():
    run(app, host='localhost', port=8080)

app = Bottle()

@app.post('/event')
def create_event():
    try:
        auth_service.validate_session(request.get_header('Authorization'))
        create_event_request = CreateEventRequest.from_dict(request.json)

        created_event =  event_service.create_event(create_event_request)

        return HTTPResponse(
            body=json.dumps(CreateEventResponse.to_dict(created_event)),
            status=200,
            headers={'Content-Type': 'application/json'}
        )
    except Exception as e:
        return exception_handler.handler(e)

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
