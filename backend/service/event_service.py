from classes.request import Event

from classes.response import CreateEventResponse

import dao.event_dao as ed
import dao.auth_dao as ad

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

def delete_event(user_id: str, request: Event):
    try:
        ed.delete_event(user_id, request.event_id)
    except Exception as e:
        raise ValueError("Error in deleting event.")
    
    return CreateEventResponse(message="Event deleted successfully", request=request)


def get_events_self(user_id: str):
    events = ed.get_events_self(user_id)
    events_response = []

    for event in events:
        events_response.append(Event.to_dict(event))

    return events_response

def get_events_other(user_id: str, owner_id: str):
    if not ad.is_user_in_contact_list(user_id, owner_id):
        raise ValueError("User unable to access events- not in contact list.")
    else:
        return get_events_self(owner_id)
