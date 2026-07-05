"""SOL parsing primitives for E-OS."""


def parse_sol(text: str) -> dict:
    """Parse a simple SOL input string into a normalized payload."""
    normalized = text.strip()
    tokens = [t for t in normalized.split(" ") if t]
    return {
        "raw": normalized,
        "tokens": tokens,
        "token_count": len(tokens),
    }
