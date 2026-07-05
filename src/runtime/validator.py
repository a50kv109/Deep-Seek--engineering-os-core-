"""Validation for runtime events."""

from core.eir import EIREvent


class Validator:
    """Checks event structure and kind."""

    allowed_kinds = {"SOL", "NAV", "TASK"}

    def validate(self, event: EIREvent) -> bool:
        return event.kind in self.allowed_kinds and isinstance(event.payload, dict)
