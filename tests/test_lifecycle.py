from domain.lifecycle import Lifecycle


def test_lifecycle_transitions():
    lc = Lifecycle()
    assert lc.state == "created"
    assert lc.start() == "running"
    assert lc.stop() == "stopped"
