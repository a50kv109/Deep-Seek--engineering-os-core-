from nav.book_nav import BookNavigator


def test_book_nav_finds_chapter():
    nav = BookNavigator()
    nav.add("Chapter 1")
    assert nav.find_chapter("Chapter 1")
