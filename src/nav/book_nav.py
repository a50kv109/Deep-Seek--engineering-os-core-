"""Book navigation adapter."""

from nav.base import BaseNavigator


class BookNavigator(BaseNavigator):
    def find_chapter(self, chapter_name: str) -> bool:
        return chapter_name in self.list()
