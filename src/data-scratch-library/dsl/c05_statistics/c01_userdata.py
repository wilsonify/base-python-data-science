import json
from dataclasses import dataclass, asdict

from dsl.c04_linear_algebra import Vector


@dataclass
class UserData:
    daily_minutes: Vector
    num_friends: Vector

    def to_json(self, path):
        """Convert the UserData instance to a JSON string."""
        with open(path, "w") as json_file:
            json.dump(asdict(self), json_file)

    @classmethod
    def from_json(cls, path):
        """Create a UserData instance from a JSON string."""
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return cls(
            daily_minutes=data["daily_minutes"],
            num_friends=data["num_friends"]
        )
