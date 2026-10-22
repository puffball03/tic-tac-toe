EMPTY = " "
class Board:
    def __init__(self, size=3):
        self._size = size
        self._grid = [[EMPTY] * size for _ in range(size)]
    @property
    def size(self):
        return self._size
    def __str__(self):
        separator = "-+-".join("-" * self._size)
        lines = []
        