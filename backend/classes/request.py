from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CreateEventRequest:
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreateEventRequest':
        try:
            assert isinstance(obj, dict)
            name = from_str(obj.get("name"))
            return CreateEventRequest(name)
        except (KeyError, ValueError, TypeError, AssertionError) as e:
            # If required fields are missing or age is not a valid integer
            raise ValueError("Invalid request data")

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        return result