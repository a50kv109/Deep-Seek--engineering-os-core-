from core.eir import make_event
from runtime.handler import Handler


def test_handler_processes_valid_event():
    h = Handler()
    out = h.handle(make_event("SOL", {"msg": "ok"}))
    assert out["status"] == "ok"


def test_handler_rejects_invalid_event():
    h = Handler()
    out = h.handle(make_event("BAD", {"msg": "no"}))
    assert out["status"] == "error"
