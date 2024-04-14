from classes.request import Event

from classes.response import CreateEventResponse

import dao.event_dao as ed

def create_event(request: Event):
    #sql code to persist data
    ed.persist_event(request)
    return CreateEventResponse(message="Created successfully", request=request)

def edit_event(user_id:str, request: Event):
    #sql code to persist data
    event = ed.get_events_self_event_id(user_id, request.event_id)
    request_dict = Event.to_dict(request)
    event.from_dict(request_dict)
    ed.persist_event(request)
    return CreateEventResponse(message="Created successfully", request=request)

def get_events_self(user_id: str):
    events = ed.get(user_id)
    events_response = []

    for event in events:
        events_response.append(Event.to_dict(event))

    return events_response