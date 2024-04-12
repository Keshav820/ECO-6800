from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast
from classes.request import CreateEventRequest


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()

@dataclass
class CreateEventResponse:
    message: str
    request: CreateEventRequest

    @staticmethod
    def from_dict(obj: Any) -> 'CreateEventResponse':
        assert isinstance(obj, dict)
        message = from_str(obj.get("message"))
        request = CreateEventRequest.from_dict(obj.get("request"))
        return CreateEventResponse(message, request)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_str(self.message)
        result["request"] = to_class(CreateEventRequest, self.request)
        return result
    
def create_event_response_from_dict(s: Any) -> CreateEventResponse:
    return CreateEventResponse.from_dict(s)


def create_event_response_to_dict(x: CreateEventResponse) -> Any:
    return to_class(CreateEventResponse, x)