from core.eir import make_event
from runtime.validator import Validator


def test_validator_accepts_allowed_kind():
    v = Validator()
    assert v.validate(make_event("SOL", {"ok": True}))


def test_validator_rejects_unknown_kind():
    v = Validator()
    assert not v.validate(make_event("UNKNOWN", {"ok": True}))
