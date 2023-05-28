import tkinter as tk
from tkinter import messagebox
import random
from tkinter.font import Font

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.x_score = 0
        self.o_score = 0

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#F4F4F4")

        self.x_score_label = tk.Label(self.window, text="You: 0", font=("Arial", 16), bg="#F4F4F4", fg="#333333")
        self.x_score_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        self.o_score_label = tk.Label(self.window, text="Bot: 0", font=("Arial", 16), bg="#F4F4F4", fg="#333333")
        self.o_score_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        font = Font(family="Helvetica", size=20, weight="bold")

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=font,
                    width=10,
                    height=5,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    bg="#FFFFFF",
                    fg="#333333",
                    relief="flat",
                    activebackground="#E0E0E0",
                    activeforeground="#333333",
                    bd=0,
                    
        
                )
                button.grid(row=i+2, column=j, padx=10, pady=10)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                winner = self.current_player
                self.update_scores(winner)
                self.display_winner(winner)
                self.window.after(1000, self.reset_scorecards)
                self.reset_board()
            elif self.check_draw():
                self.reset_board()
                self.x_score_label.config(text="Its a Tie!" ,font=("Tisa", 20))
                self.o_score_label.config(text="")
                self.window.after(1000, self.reset_scorecards)
                
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.window.after(300, self.make_bot_move)

    def update_scores(self, winner):
        if winner == "X":
            self.x_score += 1
        else:
            self.o_score += 1

    def display_winner(self, winner):
        if winner == "X":
            self.x_score_label.config(text="You wins!" ,font=("Tisa", 20))
            self.o_score_label.config(text="")
        else:
            self.x_score_label.config(text="You Lost!",font=("Helvetica", 20))
            self.o_score_label.config(text="")

    def reset_scorecards(self):
        self.x_score_label.config(text=f"X: {self.x_score}", font=("Arial", 16))
        self.o_score_label.config(text=f"O: {self.o_score}")

    # Rest of the code...


    def make_bot_move(self):
        best_score = float("-inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.make_move(row, col)

    def minimax(self, board, depth, is_maximizing):
        scores = {
            "X": -1,
            "O": 1,
            "draw": 0
        }

        winner = self.check_winner()
        if winner:
            return scores[winner]

        if self.check_draw():
            return scores["draw"]

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return ""

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

    def start(self):
        self.window.mainloop()

game = TicTacToe()
game.start()