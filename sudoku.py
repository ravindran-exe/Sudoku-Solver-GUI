import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()


        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_rowconfigure(10, weight=1)
        self.root.grid_rowconfigure(11, weight=1)
        self.root.grid_rowconfigure(12, weight=1)
        self.root.grid_columnconfigure(9, weight=1)


        self.root.geometry("450x500")

    def create_grid(self):
        vcmd = (self.root.register(self.validate_input), '%P')
        for row in range(9):
            for col in range(9):
                bg_color = "white" if (row // 3 + col // 3) % 2 == 0 else "lightgray"
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', relief='solid', bd=1, bg=bg_color, fg='black', validate='key', validatecommand=vcmd)
                entry.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
                self.entries[row][col] = entry
                entry.bind("<KeyPress>", self.on_key_press)

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=10, column=3, columnspan=3, sticky='nsew')
        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        clear_button.grid(row=11, column=3, columnspan=3, sticky='nsew')
        made_by_label = tk.Label(self.root, text="Made by Ravindran", fg='gray', cursor="hand2")
        made_by_label.grid(row=12, column=3, columnspan=3, sticky='nsew')
        made_by_label.bind("<Button-1>", lambda e: self.open_link())

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)

    def validate_input(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        if value_if_allowed.isdigit() and 1 <= int(value_if_allowed) <= 9:
            return True
        return False

    def find_empty_position(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, board, num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if board[i][j] == num:
                    return False

        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
