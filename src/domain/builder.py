"""Domain model builder."""


def build_domain(name: str, metadata: dict | None = None) -> dict:
    return {
        "name": name,
        "metadata": metadata or {},
        "version": "2.20",
    }
