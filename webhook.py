import json
from init import logger


class Event:
    """
    [Instance fields]
    - event_type: str
    - payload: dict
    - repository: dict

    """
    @staticmethod
    def factory(event_type, payload):
        if isinstance(payload, str):
            payload = json.dumps(payload)
        elif isinstance(payload, dict):
            pass
        else:
            logger.error(f"Wrong type of payload: {type(payload)}")

        if event_type == "push":
            return Push(event_type, payload)
        else:
            logger.error(f"Unhandled event type: {event_type}")

    def __init__(self, event_type: str, payload: dict):
        self.event_type = event_type
        self.payload = payload
        self.repository = payload.get("repository")

    def get_repository_name(self, full_name=False) -> str:
        if full_name:
            return self.repository.get("full_name")
        else:
            return self.repository.get("name")

    def is_triggering_event(self) -> bool:
        return False


class Push(Event):
    def __init__(self, event_type, payload):
        super().__init__(event_type, payload)

    def is_triggering_event(self) -> bool:
        ref = self.payload.get("ref")

        if not ref:
            logger.error("There is no info for 'ref' in payload.")
            return False

        return ref == "refs/heads/master"


