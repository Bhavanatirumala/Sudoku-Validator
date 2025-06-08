import tkinter as tk
from tkinter import messagebox
from sudoku_validator import SudokuValidator

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Validator")
        
        # Create main frame
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(expand=True, fill='both')
        
        # Create grid frame
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack(pady=10)
        
        # Create 9x9 grid of entry widgets
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(self.grid_frame, width=2, font=('Arial', 16))
                entry.grid(row=i, column=j, padx=1, pady=1)
                # Add some visual separation for 3x3 boxes
                if i % 3 == 0 and i != 0:
                    entry.grid(pady=(10, 1))
                if j % 3 == 0 and j != 0:
                    entry.grid(padx=(10, 1))
                row.append(entry)
            self.entries.append(row)
        
        # Create buttons frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)
        
        # Validate button
        self.validate_button = tk.Button(self.button_frame, text="Validate", command=self.validate_board)
        self.validate_button.pack(side=tk.LEFT, padx=5)
        
        # Custom Zones button
        self.zones_button = tk.Button(self.button_frame, text="Custom Zones", command=self.show_zones_dialog)
        self.zones_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_board)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Result label
        self.result_label = tk.Label(self.main_frame, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)
        
        # Custom zones
        self.custom_zones = []
        
    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                try:
                    num = int(value) if value else 0
                    if num < 0 or num > 9:
                        raise ValueError
                    row.append(num)
                except ValueError:
                    messagebox.showerror("Error", f"Invalid value at position ({i+1}, {j+1}). Use numbers 0-9 only.")
                    return None
            board.append(row)
        return board
    
    def validate_board(self):
        board = self.get_board()
        if board is None:
            return
        
        validator = SudokuValidator(self.custom_zones)
        is_valid, error = validator.validate(board)
        
        if is_valid:
            self.result_label.config(text="Valid Sudoku board!", fg="green")
        else:
            self.result_label.config(text=f"Invalid: {error}", fg="red")
    
    def show_zones_dialog(self):
        # Create a new window for custom zones input
        zones_window = tk.Toplevel(self.root)
        zones_window.title("Custom Zones")
        zones_window.geometry("400x300")
        
        # Add instructions
        instructions = tk.Label(zones_window, text="Enter custom zones (one per line):\nFormat: x1,y1 x2,y2 x3,y3 ...\nExample: 0,0 1,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8")
        instructions.pack(pady=10)
        
        # Add text area for zones
        text_area = tk.Text(zones_window, height=10, width=40)
        text_area.pack(pady=10)
        
        # Add current zones if any
        if self.custom_zones:
            for zone in self.custom_zones:
                text_area.insert(tk.END, " ".join(f"{i},{j}" for i, j in zone) + "\n")
        
        def apply_zones():
            zones_text = text_area.get("1.0", tk.END).strip()
            if not zones_text:
                self.custom_zones = []
                zones_window.destroy()
                return
            
            try:
                new_zones = []
                for line in zones_text.split("\n"):
                    if not line.strip():
                        continue
                    zone = []
                    for coord in line.split():
                        i, j = map(int, coord.split(","))
                        if i < 0 or i > 8 or j < 0 or j > 8:
                            raise ValueError
                        zone.append((i, j))
                    if len(zone) != 9:
                        raise ValueError
                    new_zones.append(zone)
                self.custom_zones = new_zones
                zones_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid zone format. Each zone must contain exactly 9 valid coordinates (0-8).")
        
        # Add Apply button
        apply_button = tk.Button(zones_window, text="Apply Zones", command=apply_zones)
        apply_button.pack(pady=10)
    
    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
        self.result_label.config(text="")
        self.custom_zones = []

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop() 