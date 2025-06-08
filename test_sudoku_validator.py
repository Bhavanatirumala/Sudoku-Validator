import unittest
from sudoku_validator import SudokuValidator

class TestSudokuValidator(unittest.TestCase):
    def setUp(self):
        # Define a valid Sudoku board
        self.valid_board = [
            [5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]
        ]
        
        # Define a custom zone (in this case, it's the same as the top-left 3x3 box)
        self.custom_zones = [
            [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        ]
        
        self.validator = SudokuValidator(self.custom_zones)
        
    def test_valid_board(self):
        """Test a valid Sudoku board."""
        is_valid, error = self.validator.validate(self.valid_board)
        self.assertTrue(is_valid)
        self.assertIsNone(error)
        
    def test_invalid_row(self):
        """Test a board with an invalid row."""
        board = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,7,8,9,1,2,3,4,5],
            [9,1,2,3,4,5,6,7,8]
        ]
        # Introduce a duplicate in row 0
        board[0][0] = 2
        validator = SudokuValidator([])  # No custom zones
        is_valid, error = validator.validate(board)
        self.assertFalse(is_valid)
        self.assertIn("Row", error)
        
    def test_invalid_column(self):
        """Test a board with an invalid column only (no row violation)."""
        board = [
            [1,0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0,0],
            [3,0,0,0,0,0,0,0,0],
            [4,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0],
            [6,0,0,0,0,0,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [8,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0]  # Duplicate '1' in column 0
        ]
        validator = SudokuValidator([])
        is_valid, error = validator.validate(board)
        self.assertFalse(is_valid)
        self.assertIn("Column", error)
        
    def test_invalid_box(self):
        """Test a board with an invalid 3x3 box only (no row/col violation)."""
        board = [
            [1,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        validator = SudokuValidator([])
        is_valid, error = validator.validate(board)
        self.assertFalse(is_valid)
        self.assertIn("Box", error)
        
    def test_invalid_custom_zone(self):
        """Test a board with an invalid custom zone (duplicate in zone, not in row/col/box)."""
        board = [
            [1,2,3,4,5,6,7,8,9],
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,7,8,9,1,2,3,4,5],
            [9,1,2,3,4,5,6,7,8]
        ]
        # Scattered custom zone (no two cells in the same row, column, or box)
        custom_zone = [(0,0), (1,3), (2,6), (3,1), (4,4), (5,7), (6,2), (7,5), (8,8)]
        # Introduce a duplicate in the custom zone
        board[0][0] = 5
        board[4][4] = 5  # Now '5' appears twice in the custom zone, but not in any row/col/box
        validator = SudokuValidator([custom_zone])
        is_valid, error = validator.validate(board)
        self.assertFalse(is_valid)
        self.assertIn("Custom zone", error)
        
    def test_invalid_size(self):
        """Test a board with invalid size."""
        invalid_board = [[1,2,3], [4,5,6], [7,8,9]]
        is_valid, error = self.validator.validate(invalid_board)
        self.assertFalse(is_valid)
        self.assertIn("Board must be 9x9", error)
        
    def test_invalid_numbers(self):
        """Test a board with numbers outside 1-9 range."""
        board = [
            [1,2,3,4,5,6,7,8,10],  # 10 is invalid
            [4,5,6,7,8,9,1,2,3],
            [7,8,9,1,2,3,4,5,6],
            [2,3,4,5,6,7,8,9,1],
            [5,6,7,8,9,1,2,3,4],
            [8,9,1,2,3,4,5,6,7],
            [3,4,5,6,7,8,9,1,2],
            [6,7,8,9,1,2,3,4,5],
            [9,1,2,3,4,5,6,7,8]
        ]
        validator = SudokuValidator([])
        is_valid, error = validator.validate(board)
        self.assertFalse(is_valid)
        self.assertIn("only digits 0-9", error)
        
    def test_multiple_custom_zones(self):
        """Test a board with multiple custom zones."""
        # Create a new custom zone (in this case, it's the bottom-right 3x3 box)
        new_zones = self.custom_zones + [
            [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
        ]
        validator = SudokuValidator(new_zones)
        is_valid, error = validator.validate(self.valid_board)
        self.assertTrue(is_valid)
        self.assertIsNone(error)

if __name__ == '__main__':
    unittest.main() 