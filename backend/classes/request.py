from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class Event:
    event_id: str
    event_name: str
    start_time: str
    end_time: str
    created_by: str

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        try:
            assert isinstance(obj, dict)
            event_id = from_str(obj.get("event_id"))
            event_name = from_str(obj.get("event_name"))
            start_time = from_str(obj.get("start_time"))
            end_time = from_str(obj.get("end_time"))
            created_by = from_str(obj.get("created_by"))
            return Event(event_id, event_name, start_time, end_time, created_by)
        except (KeyError, ValueError, TypeError, AssertionError) as e:
            raise ValueError("Invalid request data")

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_id"] = from_str(self.event_id)
        result["event_name"] = from_str(self.event_name)
        result["start_time"] = from_str(self.start_time)
        result["end_time"] = from_str(self.end_time)
        result["created_by"] = from_str(self.created_by)
        return result