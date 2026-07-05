"""Runtime engine implementation."""

from core.eir import EIREvent


class Engine:
    """Processes validated events."""

    def process(self, event: EIREvent) -> dict:
        return {
            "status": "ok",
            "kind": event.kind,
            "payload": event.payload,
        }
