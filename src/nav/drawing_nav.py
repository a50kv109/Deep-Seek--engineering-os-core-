"""Drawing navigation adapter."""

from nav.base import BaseNavigator


class DrawingNavigator(BaseNavigator):
    def find_layer(self, layer_name: str) -> bool:
        return layer_name in self.list()
