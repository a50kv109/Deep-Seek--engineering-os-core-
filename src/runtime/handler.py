"""Orchestrates validation and processing."""

from runtime.engine import Engine
from runtime.validator import Validator


class Handler:
    """Entry point used by runtime for event handling."""

    def __init__(self, validator: Validator | None = None, engine: Engine | None = None) -> None:
        self.validator = validator or Validator()
        self.engine = engine or Engine()

    def handle(self, event):
        if not self.validator.validate(event):
            return {"status": "error", "reason": "invalid_event"}
        return self.engine.process(event)
