from nav.drawing_nav import DrawingNavigator


def test_drawing_nav_finds_layer():
    nav = DrawingNavigator()
    nav.add("Layer A")
    assert nav.find_layer("Layer A")
