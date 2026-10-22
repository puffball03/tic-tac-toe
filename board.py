EMPTY = " "
class Board:
    def __init__(self, size:int=3):
        self._size = size
        self._grid = [[EMPTY] * size for _ in range(size)]
        
    @property
    def size(self) -> int:
        return self._size

    def _in_range(self, row, col):
        return 0 <= row < self._size and 0 <= col < self._size

    def _is_empty(self, row, col):
        if self._in_range(row, col) and self._grid[row][col] == EMPTY:
            return True
        else:
            return False

    def place_mark(self, row: int, col: int, mark: str) -> bool:
        if self._in_range(row, col) and self._is_empty(row, col):
            self._grid[row][col] = mark
            return True
        else:
            return False
    def remove_mark(row: int, col: int) -> None:
        pass
        #TODO this
    
    def has_won(mark: str) -> bool:
        pass

    def is_full() -> bool:
        pass
    
    def __str__(self):
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)
        