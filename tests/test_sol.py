from core.sol import parse_sol


def test_parse_sol_splits_tokens():
    out = parse_sol("E START")
    assert out["raw"] == "E START"
    assert out["tokens"] == ["E", "START"]
    assert out["token_count"] == 2
