from classes.request import CreateEventRequest

from classes.response import CreateEventResponse

def create_event(request: CreateEventRequest):
    return CreateEventResponse(message="Created successfully", request=request)