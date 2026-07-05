"""EEL logging primitives."""


class EELLogger:
    """Collects lightweight in-memory logs for the runtime."""

    def __init__(self) -> None:
        self._entries = []

    def log(self, message: str) -> None:
        self._entries.append(message)

    def entries(self) -> list:
        return list(self._entries)
