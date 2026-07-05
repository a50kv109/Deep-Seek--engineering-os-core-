"""EIR event model."""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class EIREvent:
    """Event envelope used by runtime handlers."""

    kind: str
    payload: dict
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def make_event(kind: str, payload: dict) -> EIREvent:
    return EIREvent(kind=kind, payload=payload)
