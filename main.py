from random import randint
from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("This is a Tic-Tac-Toe Game.\nProgramming by: Mehrdad Najafi")
        layout.addWidget(self.label)
        self.setLayout(layout)


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]
        
        self.ui.btn_new_game.clicked.connect(self.new_game)
        self.ui.radio_btn1.setChecked(True)
        self.ui.about_btn.clicked.connect(self.show_about_window)
        
        self.p1_score = 0
        self.p2_score = 0
        self.draw_score = 0
        
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue')
                self.game[i][j].clicked.connect(partial(self.play, i, j))

        self.flag_for_player_1 = True
        self.flag_for_player_2 = True
        self.continue_game = True

    def show_about_window(self):
        self.w = AboutWindow()
        self.w.show()
    
    def play(self, i, j):
        if self.ui.radio_btn1.isChecked():
            if self.continue_game:
                if self.game[i][j].text() == '':
                    if self.flag_for_player_1:
                        self.game[i][j].setText('X')
                        self.game[i][j].setStyleSheet('color: black ; background-color: skyblue')
                        self.flag_for_player_1 = False
                    else:
                        self.game[i][j].setText('O')
                        self.game[i][j].setStyleSheet('color: white ; background-color: skyblue')
                        self.flag_for_player_1 = True
        
        elif self.ui.radio_btn2.isChecked():
            if self.continue_game:
                if self.game[i][j].text() == '':
                    if self.flag_for_player_1:
                        self.game[i][j].setText('X')
                        self.game[i][j].setStyleSheet('color: black ; background-color: skyblue')
                        self.check()

                        if self.continue_game:
                            self.flag_for_player_2 = True
                        else:
                            self.flag_for_player_2 = False
                        
                        while self.flag_for_player_2:
                            cpu_row , cpu_col = randint(0, 2) , randint(0, 2)
                            if self.game[cpu_row][cpu_col].text() == '':
                                self.game[cpu_row][cpu_col].setText('O')
                                self.game[cpu_row][cpu_col].setStyleSheet('color: white ; background-color: skyblue')
                                self.flag_for_player_2 = False
        if self.continue_game:
            self.check()

    def new_game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: skyblue')
        self.continue_game = True
        self.flag_for_player_1 = True
    
    def check(self):
        draw_msgBox = QMessageBox()
        draw_msgBox.setText("Draw")
        player1_msgBox = QMessageBox()
        player1_msgBox.setText('Player 1 Wins')
        player2_msgBox = QMessageBox()
        player2_msgBox.setText('Player 2 Wins')
        count = 0
        
        
        for i in range(3):
            if self.game[i][0].text() == 'X' and self.game[i][1].text() == 'X' and self.game[i][2].text() == 'X':
                self.game[i][0].setStyleSheet('color: black ; background-color: red')
                self.game[i][1].setStyleSheet('color: black ; background-color: red')
                self.game[i][2].setStyleSheet('color: black ; background-color: red')
                player1_msgBox.exec()
                self.continue_game = False
                self.p1_score += 1
                self.ui.p1_score.setText(f"X : {str(self.p1_score)}")
                break
            
            elif self.game[i][0].text() == 'O' and self.game[i][1].text() == 'O' and self.game[i][2].text() == 'O':
                self.game[i][0].setStyleSheet('color: white ; background-color: red')
                self.game[i][1].setStyleSheet('color: white ; background-color: red')
                self.game[i][2].setStyleSheet('color: white ; background-color: red')
                player2_msgBox.exec()
                self.continue_game = False
                self.p2_score += 1
                self.ui.p2_score.setText(f"O : {str(self.p2_score)}")
                break
        
            elif self.game[0][i].text() == 'X' and self.game[1][i].text() == 'X' and self.game[2][i].text() == 'X':
                self.game[0][i].setStyleSheet('color: black ; background-color: red')
                self.game[1][i].setStyleSheet('color: black ; background-color: red')
                self.game[2][i].setStyleSheet('color: black ; background-color: red')
                player1_msgBox.exec()
                self.continue_game = False
                self.p1_score += 1
                self.ui.p1_score.setText(f"X : {str(self.p1_score)}")
                break
            
            elif self.game[0][i].text() == 'O' and self.game[1][i].text() == 'O' and self.game[2][i].text() == 'O':
                self.game[0][i].setStyleSheet('color: white ; background-color: red')
                self.game[1][i].setStyleSheet('color: white ; background-color: red')
                self.game[2][i].setStyleSheet('color: white ; background-color: red')
                player2_msgBox.exec()
                self.continue_game = False
                self.p2_score += 1
                self.ui.p2_score.setText(f"O : {str(self.p2_score)}")
                break
        
        if self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X':
            self.game[0][0].setStyleSheet('color: black ; background-color: red')
            self.game[1][1].setStyleSheet('color: black ; background-color: red')
            self.game[2][2].setStyleSheet('color: black ; background-color: red')
            player1_msgBox.exec()
            self.continue_game = False
            self.p1_score += 1
            self.ui.p1_score.setText(f"X : {str(self.p1_score)}")

        elif self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O':
            self.game[0][0].setStyleSheet('color: white ; background-color: red')
            self.game[1][1].setStyleSheet('color: white ; background-color: red')
            self.game[2][2].setStyleSheet('color: white ; background-color: red')
            player2_msgBox.exec()
            self.continue_game = False
            self.p2_score += 1
            self.ui.p2_score.setText(f"O : {str(self.p2_score)}")
        
        elif self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X':
            self.game[0][2].setStyleSheet('color: black ; background-color: red')
            self.game[1][1].setStyleSheet('color: black ; background-color: red')
            self.game[2][0].setStyleSheet('color: black ; background-color: red')
            player1_msgBox.exec()
            self.continue_game = False
            self.p1_score += 1
            self.ui.p1_score.setText(f"X : {str(self.p1_score)}")
        
        elif self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O':
            self.game[0][2].setStyleSheet('color: white ; background-color: red')
            self.game[1][1].setStyleSheet('color: white ; background-color: red')
            self.game[2][0].setStyleSheet('color: white ; background-color: red')
            player2_msgBox.exec()
            self.continue_game = False
            self.p2_score += 1
            self.ui.p2_score.setText(f"O : {str(self.p2_score)}")
        
        elif self.continue_game:
            for i in range(3):
                for j in range(3):
                    if self.game[i][j].text() == 'X' or self.game[i][j].text() == 'O':
                        count += 1
            if count == 9:
                draw_msgBox.exec()
                self.continue_game = False
                self.draw_score += 1
                self.ui.draw_score.setText(f"Draw: {str(self.draw_score)}")
        


        
app = QApplication([])
window = TicTacToe()
app.exec()