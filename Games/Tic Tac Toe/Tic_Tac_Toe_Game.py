import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.iconbitmap(r"C:\Users\Ronakgupta\Music\PROGRAMMING\Python Programming Language\Games\Tic Tac Toe\game.ico")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('Arial', 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "The game is a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
            return True
        # Check diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ")
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()