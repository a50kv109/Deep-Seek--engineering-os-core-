"""Navigation base interfaces."""


class BaseNavigator:
    def __init__(self) -> None:
        self._items = []

    def add(self, item: str) -> None:
        self._items.append(item)

    def list(self) -> list:
        return list(self._items)
