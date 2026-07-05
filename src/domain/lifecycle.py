"""Lifecycle model for domain entities."""


class Lifecycle:
    def __init__(self) -> None:
        self.state = "created"

    def start(self) -> str:
        self.state = "running"
        return self.state

    def stop(self) -> str:
        self.state = "stopped"
        return self.state
