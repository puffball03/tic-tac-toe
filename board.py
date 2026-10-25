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

    def is_empty(self, row, col):
        if self._in_range(row, col) and self._grid[row][col] == EMPTY:
            return True
        else:
            return False
    def empty_cells(self):
        res = []
        for row in range(self._size):
            for col in range(self._size):
                if self._grid[row][col] == EMPTY:
                    res.append((row, col))
        return res
                
    def copy(self):
        new_board = Board(self._size)
        new_board._grid = [row[:] for row in self._grid]
        return new_board
    def place_mark(self, row: int, col: int, mark: str) -> bool:
        if self._in_range(row, col) and self.is_empty(row, col):
            self._grid[row][col] = mark
            return True
        else:
            return False
    def remove_mark(self, row: int, col: int) -> None:
        if self._in_range(row, col) and not self.is_empty(row, col):
            self._grid[row][col] = EMPTY

            

    def has_won(self, mark: str) -> bool:
        #Rows
        for row in self._grid:
            if all(i == mark for i in row):
                return True
        #Columns
        for col in zip(*self._grid):
            if all(i == mark for i in col):
                return True
        #Check Diagonals
        if all(self._grid[i][i] == mark for i in range(self.size)):
            return True
        if all(self._grid[i][self.size - i - 1] == mark for i in range(self.size)):
            return True
        #No wincon. Return False. LOSER!
        return False

    def is_full(self) -> bool:
        return all(i == "X" or i == "O" for row in self._grid for i in row)
                
    
    def __str__(self):
        separator = "-+-".join("-" * self._size)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)
        