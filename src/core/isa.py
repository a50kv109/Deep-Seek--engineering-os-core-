"""ISA profile definitions for E-OS."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ISAProfile:
    """A minimal instruction set profile."""

    version: str = "2.20"
    required_prefix: str = "E"

    def validate_token(self, token: str) -> bool:
        return token.startswith(self.required_prefix)
