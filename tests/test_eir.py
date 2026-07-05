from core.eir import make_event


def test_make_event_creates_envelope():
    evt = make_event("SOL", {"step": 1})
    assert evt.kind == "SOL"
    assert evt.payload["step"] == 1
    assert evt.ts
