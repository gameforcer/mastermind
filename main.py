import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from rules import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Mastermind"
        self.left = 100
        self.top = 100
        self.width = 520
        self.height = 200
        self.initUI()
        self.initPyGame()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.game_data = QLabel(self)
        self.game_data.setText("dobre pozycje:            dobre cyfry:              tura:")
        self.game_data.move(250, 0)
        self.game_data.resize(280,40)

        self.history = QLabel(self)
        self.history.setText("historia:")
        self.history.move(160, 5)

        self.history_data = QLabel(self)
        self.history_data.setText("")
        self.history_data.resize(50,155)
        self.history_data.setAlignment(Qt.AlignTop)
        self.history_data.move(160, 28)

        self.crct_pos = QLabel(self)
        self.crct_pos.setText("")
        self.crct_pos.resize(50,155)
        self.crct_pos.setAlignment(Qt.AlignTop)
        self.crct_pos.move(250, 28)

        self.crct_num = QLabel(self)
        self.crct_num.setText("")
        self.crct_num.resize(50,155)
        self.crct_num.setAlignment(Qt.AlignTop)
        self.crct_num.move(357, 28)

        self.crnt_turn = QLabel(self)
        self.crnt_turn.setText("")
        self.crnt_turn.resize(50,155)
        self.crnt_turn.setAlignment(Qt.AlignTop)
        self.crnt_turn.move(460, 28)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(100,20)
        
        self.chck_B = QPushButton('Sprawdź', self)
        self.chck_B.move(20,60)
        self.chck_B.resize(80,30)

        self.reset_B = QPushButton("Reset", self)
        self.reset_B.move(20,100)
        self.reset_B.resize(80,30)

        self.cheater_B = QPushButton("Oszust!", self)
        self.cheater_B.move(20,140)
        self.cheater_B.resize(80,30)

        self.popup = QLabel()
        self.popup.resize(80,80)
        self.popup.setAlignment(Qt.AlignCenter)
        
        checkFun = lambda x: x.chck_click 
        resetFun = lambda x: x.reset_click 
        cheaterFun = lambda x: x.cheat_click 

        self.chck_B.clicked.connect(checkFun(self))
        self.reset_B.clicked.connect(resetFun(self))
        self.cheater_B.clicked.connect(cheaterFun(self))
        self.show()
    
    def initPyGame(self):
        self.reset_click()

    @pyqtSlot()
    def chck_click(self):
        self.s = self.textbox.text()
        self.guess_vals = [int(c) for c in self.s if c in '123456']
        print(self.guess_vals)
        if not hasattr(self.game, "_result_flag") and len(self.guess_vals) == 4 and len(self.s) == 4:
            self.game.setGuess(self.guess_vals)
            self.game.runTurn()

            #printed data updates
            self.crct_pos.setText(self.crct_pos.text()+str(self.game.getCrctPos())+'\n')
            self.crct_num.setText(self.crct_num.text()+str(self.game.getCrctNum())+'\n')
            self.crnt_turn.setText(self.crnt_turn.text()+str(self.game.getTries())+'\n')
            self.history_data.setText(self.history_data.text()+self.s+'\n')
            self.textbox.setText("")
            
            if hasattr(self.game, "_result_flag"):
                if self.game._result_flag:
                    self.popup.setText("Wygrana")
                else:
                    self.popup.setText("Przegrana")
                self.popup.show()

    @pyqtSlot()
    def reset_click(self):
        if randint(0, 2):
            self.game = normalMode()
            print("NORMAL MODE ON")
        else:
            self.game = cheatMode()
            print("CHEAT MODE ON")
        
        self.history_data.setText("")
        self.crct_pos.setText("")
        self.crct_num.setText("")
        self.crnt_turn.setText("")
        self.textbox.setText("")
    
    @pyqtSlot()
    def cheat_click(self):
        if isinstance(self.game, cheatMode) and not hasattr(self.game, "_result_flag"):
            self.popup.setText("Złapałeś/łaś mnie!")
            self.game._result_flag = True
        else:
            self.popup.setText("Tere fere\n"+str(self.game._key))
            self.game._result_flag = False
        self.popup.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
