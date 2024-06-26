# GAME Base for RL agent (testing new funcs etc.)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt

L = 3 #rows
R = 3 #cols


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.board = [[' ' for _ in range(L)] for _ in range(R)]
        self.current_player = "X"
        self.moves = 0

        self.layout = QGridLayout()

        for i in range(L):
            for j in range(R):
                button = QPushButton('')
                button.clicked.connect(lambda ch, r=i, c=j: self.make_move(r, c))
                self.layout.addWidget(button, i, j)

        self.setLayout(self.layout)

        self.setWindowTitle('Tic Tac Toe')
        self.show()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.display_board()
            self.moves += 1
            if self.check_win():
                self.game_over(f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.moves == L*R:
                self.game_over("It's a tie!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def display_board(self):
        for i in range(L):
            for j in range(R):
                button = self.layout.itemAtPosition(i, j).widget()
                button.setText(self.board[i][j])

    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        for col in range(L):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def game_over(self, message):
        winner_label = QLabel(message)
        winner_label.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(winner_label, L, 0, 1, R)
        self.setLayout(self.layout)

    def disable_buttons(self):
        for i in range(L):
            for j in range(R):
                button = self.layout.itemAtPosition(i, j).widget()
                button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())