class SudokuValidator:
    def __init__(self, custom_zones=None):
        """
        Initialize the Sudoku validator.
        :param custom_zones: List of custom zones, each zone is a list of (row, col) tuples.
        """
        self.custom_zones = custom_zones or []

    def validate(self, board):
        """
        Validate a 9x9 Sudoku board.
        :param board: 2D list representing the Sudoku board.
        :return: Tuple (is_valid, error_message). If valid, error_message is None.
        """
        # Check board size
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False, "Board must be 9x9."

        # Check for numbers outside 0, 1-9
        for row in board:
            for num in row:
                if num not in range(0, 10):
                    return False, "Board must contain only digits 0-9 (0 for empty)."

        # Check custom zones first
        for zone in self.custom_zones:
            seen = set()
            for i, j in zone:
                num = board[i][j]
                if num == 0:
                    continue
                if num in seen:
                    return False, "Custom zone does not contain unique digits 1-9."
                seen.add(num)

        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[i][j]
                if num == 0:
                    continue
                if num in seen:
                    return False, f"Row {i+1} does not contain unique digits 1-9."
                seen.add(num)

        # Check columns
        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]
                if num == 0:
                    continue
                if num in seen:
                    return False, f"Column {j+1} does not contain unique digits 1-9."
                seen.add(num)

        # Check 3x3 boxes
        for box_i in range(3):
            for box_j in range(3):
                seen = set()
                for i in range(3 * box_i, 3 * (box_i + 1)):
                    for j in range(3 * box_j, 3 * (box_j + 1)):
                        num = board[i][j]
                        if num == 0:
                            continue
                        if num in seen:
                            return False, f"Box at ({box_i+1},{box_j+1}) does not contain unique digits 1-9."
                        seen.add(num)

        return True, None 