import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [for  in range(9)]

        self.buttons = [tk.Button(root, text=" ", font=('Arial', 24), width=5, height=2,
                                   command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Victory!", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Draw!", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [for  in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

if _name == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()