# Sudoku Validator with Custom Zones

A Python-based Sudoku validator with a graphical user interface (GUI) that validates 9x9 Sudoku boards, including support for custom zones. The validator checks standard Sudoku rules (rows, columns, 3x3 boxes) and any user-defined zones for uniqueness of digits 1-9.

## Quick Start
To validate a Sudoku board, simply run:
```bash
python sudoku_gui.py
```
This will open the GUI where you can enter your board and get immediate validation results.

## Features
- Interactive 9x9 grid interface
- Support for standard Sudoku rules
- Custom zone validation (e.g., diagonals, Windoku)
- Clear visual feedback for validation results
- Easy-to-use custom zone input
- Support for both filled and partially filled boards (0 for empty cells)

## Setup
1. Ensure you have Python 3.6+ installed
2. Clone or download this repository
3. No additional dependencies required (uses only Python standard library and Tkinter)

## Using the GUI (Main Interface)

### Basic Usage
1. **Enter Numbers**:
   - Type numbers 1-9 in the cells
   - Use 0 or leave blank for empty cells
   - The grid has visual separators for 3x3 boxes

2. **Validate Board**:
   - Click "Validate" to check if the board is valid
   - Results appear below the grid:
     - Green text: Valid board
     - Red text: Invalid board with error message

3. **Custom Zones**:
   - Click "Custom Zones" button
   - Enter coordinates in format: `x1,y1 x2,y2 x3,y3 ...`
   - Example for main diagonal: `0,0 1,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8`
   - Click "Apply Zones"

4. **Clear Board**:
   - Click "Clear" to reset the board and custom zones

### Example Custom Zones

#### Diagonal Sudoku
```
0,0 1,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8
0,8 1,7 2,6 3,5 4,4 5,3 6,2 7,1 8,0
```

#### Windoku (Extra 3x3 Regions)
```
1,1 1,2 1,3 2,1 2,2 2,3 3,1 3,2 3,3
1,5 1,6 1,7 2,5 2,6 2,7 3,5 3,6 3,7
5,1 5,2 5,3 6,1 6,2 6,3 7,1 7,2 7,3
5,5 5,6 5,7 6,5 6,6 6,7 7,5 7,6 7,7
```

## Test Cases
The `gui_test_cases.txt` file contains various test cases you can use:
- Valid standard Sudoku
- Invalid row/column/box
- Valid/invalid diagonal Sudoku
- Partially filled boards
- Custom zone examples
- Windoku examples

To use a test case:
1. Open `gui_test_cases.txt`
2. Copy the board (9 lines of numbers)
3. Paste into the GUI grid
4. If the test case has custom zones, add them using the "Custom Zones" button

## Project Structure
- `sudoku_gui.py` — Main GUI application (run this to validate boards)
- `sudoku_validator.py` — Core validation logic (used by GUI)
- `gui_test_cases.txt` — Collection of test cases for the GUI
- `test_sudoku_validator.py` — Unit tests for developers
- `README.md` — This documentation

## For Developers
If you're interested in the validation logic or want to run the test suite:
```bash
python -m unittest test_sudoku_validator.py
```

## License
MIT 