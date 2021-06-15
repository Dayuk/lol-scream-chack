from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QLabel
import sys
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
# import sqlite3
# from collections import Counter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# con = sqlite3.connect("Tournament Data.db")
# cur = con.cursor()

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.chll = ['46','61','61','54','44']
        self.grm = ['44', '58', '56', '50', '43']
        self.master = ['42','52','51','47','42']
        self.D12 = ['37', '47', '46', '38', '38']
        self.D34 = ['32', '38', '37', '30', '34']
        self.pla = ['27', '29', '29', '23', '29']
        self.gld = ['22', '20', '18', '16', '25']
        self.slv = ['17', '10', '10', '8', '20']
        self.blz = ['12', '2', '1', '1', '16']
        self.iorn = ['7', '-4', '-5', '-3', '12']

        self.Wlabel = QLabel('        VS        ', self)
        self.Wlabel.move(330, 80)
        self.Wlabel.setAlignment(Qt.AlignVCenter)
        font1 = self.Wlabel.font()
        font1.setPointSize(20)
        font1.setFamily('Times New Roman')
        font1.setBold(True)
        self.Wlabel.setFont(font1)

        label1 = QLabel('Blue Team Score:', self)
        label1.move(100, 200)
        self.Blabel = QLabel('000', self)
        self.Blabel.move(210, 200)

        label1 = QLabel('TOP', self)
        label1.move(10, 10)
        label1 = QLabel('닉네임:', self)
        label1.move(50, 10)
        self.Nick1 = QLineEdit(self)
        self.Nick1.resize(100,20)
        self.Nick1.move(95, 7)
        self.Tear2 = QComboBox(self)
        self.Tear2.addItem('Tear')
        self.Tear2.addItem('Challenger')
        self.Tear2.addItem('GrandMaster')
        self.Tear2.addItem('Master')
        self.Tear2.addItem('Diamond 1,2')
        self.Tear2.addItem('Diamond 3,4')
        self.Tear2.addItem('Platinum')
        self.Tear2.addItem('Gold')
        self.Tear2.addItem('Silver')
        self.Tear2.addItem('Bronze')
        self.Tear2.addItem('Iorn')
        self.Tear2.resize(100, 20)
        self.Tear2.move(200, 7)
        self.Blabel1 = QLabel('00', self)
        self.Blabel1.move(310, 12)
        self.Tear2.currentIndexChanged.connect(self.Score1)
        self.Tear2.currentIndexChanged.connect(self.BTeamScore)
        self.Tear2.currentIndexChanged.connect(self.Win)

        label1 = QLabel(' JG', self)
        label1.move(10, 50)
        label1 = QLabel('닉네임:', self)
        label1.move(50, 50)
        self.Nick2 = QLineEdit(self)
        self.Nick2.resize(100,20)
        self.Nick2.move(95, 47)
        self.Tear3 = QComboBox(self)
        self.Tear3.addItem('Tear')
        self.Tear3.addItem('Challenger')
        self.Tear3.addItem('GrandMaster')
        self.Tear3.addItem('Master')
        self.Tear3.addItem('Diamond 1,2')
        self.Tear3.addItem('Diamond 3,4')
        self.Tear3.addItem('Platinum')
        self.Tear3.addItem('Gold')
        self.Tear3.addItem('Silver')
        self.Tear3.addItem('Bronze')
        self.Tear3.addItem('Iorn')
        self.Tear3.resize(100, 20)
        self.Tear3.move(200, 47)
        self.Blabel2 = QLabel('00', self)
        self.Blabel2.move(310, 52)
        self.Tear3.currentIndexChanged.connect(self.Score2)
        self.Tear3.currentIndexChanged.connect(self.BTeamScore)
        self.Tear3.currentIndexChanged.connect(self.Win)

        label1 = QLabel('MID', self)
        label1.move(10, 90)
        label1 = QLabel('닉네임:', self)
        label1.move(50, 90)
        self.Nick3 = QLineEdit(self)
        self.Nick3.resize(100,20)
        self.Nick3.move(95, 87)
        self.Tear4 = QComboBox(self)
        self.Tear4.addItem('Tear')
        self.Tear4.addItem('Challenger')
        self.Tear4.addItem('GrandMaster')
        self.Tear4.addItem('Master')
        self.Tear4.addItem('Diamond 1,2')
        self.Tear4.addItem('Diamond 3,4')
        self.Tear4.addItem('Platinum')
        self.Tear4.addItem('Gold')
        self.Tear4.addItem('Silver')
        self.Tear4.addItem('Bronze')
        self.Tear4.addItem('Iorn')
        self.Tear4.resize(100, 20)
        self.Tear4.move(200, 87)
        self.Blabel3 = QLabel('00', self)
        self.Blabel3.move(310, 92)
        self.Tear4.currentIndexChanged.connect(self.Score3)
        self.Tear4.currentIndexChanged.connect(self.BTeamScore)
        self.Tear4.currentIndexChanged.connect(self.Win)

        label1 = QLabel(' AD', self)
        label1.move(10, 130)
        label1 = QLabel('닉네임:', self)
        label1.move(50, 130)
        self.Nick4 = QLineEdit(self)
        self.Nick4.resize(100,20)
        self.Nick4.move(95, 127)
        self.Tear5 = QComboBox(self)
        self.Tear5.addItem('Tear')
        self.Tear5.addItem('Challenger')
        self.Tear5.addItem('GrandMaster')
        self.Tear5.addItem('Master')
        self.Tear5.addItem('Diamond 1,2')
        self.Tear5.addItem('Diamond 3,4')
        self.Tear5.addItem('Platinum')
        self.Tear5.addItem('Gold')
        self.Tear5.addItem('Silver')
        self.Tear5.addItem('Bronze')
        self.Tear5.addItem('Iorn')
        self.Tear5.resize(100, 20)
        self.Tear5.move(200, 127)
        self.Blabel4 = QLabel('00', self)
        self.Blabel4.move(310, 132)
        self.Tear5.currentIndexChanged.connect(self.Score4)
        self.Tear5.currentIndexChanged.connect(self.BTeamScore)
        self.Tear5.currentIndexChanged.connect(self.Win)

        label1 = QLabel('SUP', self)
        label1.move(10, 170)
        label1 = QLabel('닉네임:', self)
        label1.move(50, 170)
        self.Nick5 = QLineEdit(self)
        self.Nick5.resize(100,20)
        self.Nick5.move(95, 167)
        self.Tear6 = QComboBox(self)
        self.Tear6.addItem('Tear')
        self.Tear6.addItem('Challenger')
        self.Tear6.addItem('GrandMaster')
        self.Tear6.addItem('Master')
        self.Tear6.addItem('Diamond 1,2')
        self.Tear6.addItem('Diamond 3,4')
        self.Tear6.addItem('Platinum')
        self.Tear6.addItem('Gold')
        self.Tear6.addItem('Silver')
        self.Tear6.addItem('Bronze')
        self.Tear6.addItem('Iorn')
        self.Tear6.resize(100, 20)
        self.Tear6.move(200, 167)
        self.Blabel5 = QLabel('00', self)
        self.Blabel5.move(310, 172)
        self.Tear6.currentIndexChanged.connect(self.Score5)
        self.Tear6.currentIndexChanged.connect(self.BTeamScore)
        self.Tear6.currentIndexChanged.connect(self.Win)

        label1 = QLabel(':Red Team Score', self)
        label1.move(600, 200)
        self.Rlabel = QLabel('000', self)
        self.Rlabel.move(575, 200)

        label1 = QLabel('TOP', self)
        label1.move(765, 11)
        label1 = QLabel(':닉네임', self)
        label1.move(710, 11)
        self.Nick6 = QLineEdit(self)
        self.Nick6.resize(100,20)
        self.Nick6.move(605, 7)
        self.Tearr = QComboBox(self)
        self.Tearr.addItem('Tear')
        self.Tearr.addItem('Challenger')
        self.Tearr.addItem('GrandMaster')
        self.Tearr.addItem('Master')
        self.Tearr.addItem('Diamond 1,2')
        self.Tearr.addItem('Diamond 3,4')
        self.Tearr.addItem('Platinum')
        self.Tearr.addItem('Gold')
        self.Tearr.addItem('Silver')
        self.Tearr.addItem('Bronze')
        self.Tearr.addItem('Iorn')
        self.Tearr.resize(100, 20)
        self.Tearr.move(500, 7)
        self.Rlabel1 = QLabel('00', self)
        self.Rlabel1.move(480, 12)
        self.Tearr.currentIndexChanged.connect(self.Score6)
        self.Tearr.currentIndexChanged.connect(self.RTeamScore)
        self.Tearr.currentIndexChanged.connect(self.Win)

        label1 = QLabel('JG ', self)
        label1.move(765, 51)
        label1 = QLabel(':닉네임', self)
        label1.move(710, 51)
        self.Nick7 = QLineEdit(self)
        self.Nick7.resize(100,20)
        self.Nick7.move(605, 47)
        self.Tearr2 = QComboBox(self)
        self.Tearr2.addItem('Tear')
        self.Tearr2.addItem('Challenger')
        self.Tearr2.addItem('GrandMaster')
        self.Tearr2.addItem('Master')
        self.Tearr2.addItem('Diamond 1,2')
        self.Tearr2.addItem('Diamond 3,4')
        self.Tearr2.addItem('Platinum')
        self.Tearr2.addItem('Gold')
        self.Tearr2.addItem('Silver')
        self.Tearr2.addItem('Bronze')
        self.Tearr2.addItem('Iorn')
        self.Tearr2.resize(100, 20)
        self.Tearr2.move(500, 47)
        self.Rlabel2 = QLabel('00', self)
        self.Rlabel2.move(480, 52)
        self.Tearr2.currentIndexChanged.connect(self.Score7)
        self.Tearr2.currentIndexChanged.connect(self.RTeamScore)
        self.Tearr2.currentIndexChanged.connect(self.Win)

        label1 = QLabel('MID', self)
        label1.move(765, 91)
        label1 = QLabel(':닉네임', self)
        label1.move(710, 91)
        self.Nick8 = QLineEdit(self)
        self.Nick8.resize(100,20)
        self.Nick8.move(605, 87)
        self.Tearr3 = QComboBox(self)
        self.Tearr3.addItem('Tear')
        self.Tearr3.addItem('Challenger')
        self.Tearr3.addItem('GrandMaster')
        self.Tearr3.addItem('Master')
        self.Tearr3.addItem('Diamond 1,2')
        self.Tearr3.addItem('Diamond 3,4')
        self.Tearr3.addItem('Platinum')
        self.Tearr3.addItem('Gold')
        self.Tearr3.addItem('Silver')
        self.Tearr3.addItem('Bronze')
        self.Tearr3.addItem('Iorn')
        self.Tearr3.resize(100, 20)
        self.Tearr3.move(500, 87)
        self.Rlabel3 = QLabel('00', self)
        self.Rlabel3.move(480, 92)
        self.Tearr3.currentIndexChanged.connect(self.Score8)
        self.Tearr3.currentIndexChanged.connect(self.RTeamScore)
        self.Tearr3.currentIndexChanged.connect(self.Win)

        label1 = QLabel('AD ', self)
        label1.move(765, 131)
        label1 = QLabel(':닉네임', self)
        label1.move(710, 131)
        self.Nick9 = QLineEdit(self)
        self.Nick9.resize(100,20)
        self.Nick9.move(605, 127)
        self.Tearr4 = QComboBox(self)
        self.Tearr4.addItem('Tear')
        self.Tearr4.addItem('Challenger')
        self.Tearr4.addItem('GrandMaster')
        self.Tearr4.addItem('Master')
        self.Tearr4.addItem('Diamond 1,2')
        self.Tearr4.addItem('Diamond 3,4')
        self.Tearr4.addItem('Platinum')
        self.Tearr4.addItem('Gold')
        self.Tearr4.addItem('Silver')
        self.Tearr4.addItem('Bronze')
        self.Tearr4.addItem('Iorn')
        self.Tearr4.resize(100, 20)
        self.Tearr4.move(500, 127)
        self.Rlabel4 = QLabel('00', self)
        self.Rlabel4.move(480, 132)
        self.Tearr4.currentIndexChanged.connect(self.Score9)
        self.Tearr4.currentIndexChanged.connect(self.RTeamScore)
        self.Tearr4.currentIndexChanged.connect(self.Win)

        label1 = QLabel('SUP', self)
        label1.move(765, 171)
        label1 = QLabel(':닉네임', self)
        label1.move(710, 171)
        self.Nickk = QLineEdit(self)
        self.Nickk.resize(100,20)
        self.Nickk.move(605, 167)
        self.Tearr5 = QComboBox(self)
        self.Tearr5.addItem('Tear')
        self.Tearr5.addItem('Challenger')
        self.Tearr5.addItem('GrandMaster')
        self.Tearr5.addItem('Master')
        self.Tearr5.addItem('Diamond 1,2')
        self.Tearr5.addItem('Diamond 3,4')
        self.Tearr5.addItem('Platinum')
        self.Tearr5.addItem('Gold')
        self.Tearr5.addItem('Silver')
        self.Tearr5.addItem('Bronze')
        self.Tearr5.addItem('Iorn')
        self.Tearr5.resize(100, 20)
        self.Tearr5.move(500, 167)
        self.Rlabel5 = QLabel('00', self)
        self.Rlabel5.move(480, 172)
        self.Tearr5.currentIndexChanged.connect(self.Score10)
        self.Tearr5.currentIndexChanged.connect(self.RTeamScore)
        self.Tearr5.currentIndexChanged.connect(self.Win)


        # label1 = QLabel('티어   : ', self)
        # label1.move(10, 40)
        # label1 = QLabel('라인   : ', self)
        # label1.move(10, 70)
        # self.Nick.textChanged[str].connect(self.NickS)
        # self.Tear.currentIndexChanged.connect(self.Score1)
        # self.Tear.activated[str].connect(self.TearS)


        # self.Line = QComboBox(self)
        # self.Line.addItem('Line')
        # self.Line.addItem('TOP')
        # self.Line.addItem('JG')
        # self.Line.addItem('MID')
        # self.Line.addItem('AD')
        # self.Line.addItem('SUP')
        # self.Line.resize(150, 25)
        # self.Line.move(55, 65)
        # self.Line.activated[str].connect(self.LineS)
        # self.Line.currentIndexChanged.connect(self.Score2)

        # self.save = QPushButton('등록', self)
        # self.save.resize(50,87)
        # self.save.move(210, 5)
        # self.save.setCheckable(True)
        # self.save.clicked.connect(self.SaveS)

        # self.delete = QPushButton('초기화', self)
        # self.delete.resize(50,87)
        # self.delete.move(263, 5)
        # self.delete.setCheckable(True)
        # self.delete.clicked.connect(self.Reset)

        # self.Table = QTableWidget(self)
        # self.Table.setRowCount(1000000)
        # self.Table.setColumnCount(4)
        # self.Table.resize(476, 300)
        # self.Table.move(10, 100)
        # self.setTableWidgetData()

        self.Reset = QPushButton('초기화', self)
        self.Reset.resize(100, 55)
        self.Reset.move(355, 190)
        self.Reset.clicked.connect(self.Resett)

        label = QLabel('Made-By : LOLTOPIA', self)
        label.setAlignment(Qt.AlignVCenter)
        font1 = label.font()
        font1.setPointSize(15)
        layout = QVBoxLayout()
        layout.addWidget(label)
        label.move(5, 235)

        self.setWindowTitle('Scream AutoTeam')
        self.setWindowIcon(QIcon('img\\icon.png'))
        self.setFixedSize(800, 250)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.center()
        self.show()

    def Resett(self):
        self.Blabel.setText('000')
        self.Blabel.repaint()
        self.Blabel1.setText('00')
        self.Blabel1.repaint()
        self.Blabel2.setText('00')
        self.Blabel2.repaint()
        self.Blabel3.setText('00')
        self.Blabel3.repaint()
        self.Blabel4.setText('00')
        self.Blabel4.repaint()
        self.Blabel5.setText('00')
        self.Blabel5.repaint()
        self.Rlabel.setText('000')
        self.Rlabel.repaint()
        self.Rlabel1.setText('00')
        self.Rlabel1.repaint()
        self.Rlabel2.setText('00')
        self.Rlabel2.repaint()
        self.Rlabel3.setText('00')
        self.Rlabel3.repaint()
        self.Rlabel4.setText('00')
        self.Rlabel4.repaint()
        self.Rlabel5.setText('00')
        self.Rlabel5.repaint()
        self.Nick1.clear()
        self.Nick2.clear()
        self.Nick3.clear()
        self.Nick4.clear()
        self.Nick5.clear()
        self.Nick6.clear()
        self.Nick7.clear()
        self.Nick8.clear()
        self.Nick9.clear()
        self.Nickk.clear()
        self.Tear2.clear()
        self.Tear3.clear()
        self.Tear4.clear()
        self.Tear5.clear()
        self.Tear6.clear()
        self.Tearr.clear()
        self.Tearr2.clear()
        self.Tearr3.clear()
        self.Tearr4.clear()
        self.Tearr5.clear()
        self.Tear2.addItem('Tear')
        self.Tear2.addItem('Challenger')
        self.Tear2.addItem('GrandMaster')
        self.Tear2.addItem('Master')
        self.Tear2.addItem('Diamond 1,2')
        self.Tear2.addItem('Diamond 3,4')
        self.Tear2.addItem('Platinum')
        self.Tear2.addItem('Gold')
        self.Tear2.addItem('Silver')
        self.Tear2.addItem('Bronze')
        self.Tear2.addItem('Iorn')
        self.Tear3.addItem('Tear')
        self.Tear3.addItem('Challenger')
        self.Tear3.addItem('GrandMaster')
        self.Tear3.addItem('Master')
        self.Tear3.addItem('Diamond 1,2')
        self.Tear3.addItem('Diamond 3,4')
        self.Tear3.addItem('Platinum')
        self.Tear3.addItem('Gold')
        self.Tear3.addItem('Silver')
        self.Tear3.addItem('Bronze')
        self.Tear3.addItem('Iorn')
        self.Tear4.addItem('Tear')
        self.Tear4.addItem('Challenger')
        self.Tear4.addItem('GrandMaster')
        self.Tear4.addItem('Master')
        self.Tear4.addItem('Diamond 1,2')
        self.Tear4.addItem('Diamond 3,4')
        self.Tear4.addItem('Platinum')
        self.Tear4.addItem('Gold')
        self.Tear4.addItem('Silver')
        self.Tear4.addItem('Bronze')
        self.Tear4.addItem('Iorn')
        self.Tear5.addItem('Tear')
        self.Tear5.addItem('Challenger')
        self.Tear5.addItem('GrandMaster')
        self.Tear5.addItem('Master')
        self.Tear5.addItem('Diamond 1,2')
        self.Tear5.addItem('Diamond 3,4')
        self.Tear5.addItem('Platinum')
        self.Tear5.addItem('Gold')
        self.Tear5.addItem('Silver')
        self.Tear5.addItem('Bronze')
        self.Tear5.addItem('Iorn')
        self.Tear6.addItem('Tear')
        self.Tear6.addItem('Challenger')
        self.Tear6.addItem('GrandMaster')
        self.Tear6.addItem('Master')
        self.Tear6.addItem('Diamond 1,2')
        self.Tear6.addItem('Diamond 3,4')
        self.Tear6.addItem('Platinum')
        self.Tear6.addItem('Gold')
        self.Tear6.addItem('Silver')
        self.Tear6.addItem('Bronze')
        self.Tear6.addItem('Iorn')
        self.Tearr.addItem('Tear')
        self.Tearr.addItem('Challenger')
        self.Tearr.addItem('GrandMaster')
        self.Tearr.addItem('Master')
        self.Tearr.addItem('Diamond 1,2')
        self.Tearr.addItem('Diamond 3,4')
        self.Tearr.addItem('Platinum')
        self.Tearr.addItem('Gold')
        self.Tearr.addItem('Silver')
        self.Tearr.addItem('Bronze')
        self.Tearr.addItem('Iorn')
        self.Tearr2.addItem('Tear')
        self.Tearr2.addItem('Challenger')
        self.Tearr2.addItem('GrandMaster')
        self.Tearr2.addItem('Master')
        self.Tearr2.addItem('Diamond 1,2')
        self.Tearr2.addItem('Diamond 3,4')
        self.Tearr2.addItem('Platinum')
        self.Tearr2.addItem('Gold')
        self.Tearr2.addItem('Silver')
        self.Tearr2.addItem('Bronze')
        self.Tearr2.addItem('Iorn')
        self.Tearr3.addItem('Tear')
        self.Tearr3.addItem('Challenger')
        self.Tearr3.addItem('GrandMaster')
        self.Tearr3.addItem('Master')
        self.Tearr3.addItem('Diamond 1,2')
        self.Tearr3.addItem('Diamond 3,4')
        self.Tearr3.addItem('Platinum')
        self.Tearr3.addItem('Gold')
        self.Tearr3.addItem('Silver')
        self.Tearr3.addItem('Bronze')
        self.Tearr3.addItem('Iorn')
        self.Tearr4.addItem('Tear')
        self.Tearr4.addItem('Challenger')
        self.Tearr4.addItem('GrandMaster')
        self.Tearr4.addItem('Master')
        self.Tearr4.addItem('Diamond 1,2')
        self.Tearr4.addItem('Diamond 3,4')
        self.Tearr4.addItem('Platinum')
        self.Tearr4.addItem('Gold')
        self.Tearr4.addItem('Silver')
        self.Tearr4.addItem('Bronze')
        self.Tearr4.addItem('Iorn')
        self.Tearr5.addItem('Tear')
        self.Tearr5.addItem('Challenger')
        self.Tearr5.addItem('GrandMaster')
        self.Tearr5.addItem('Master')
        self.Tearr5.addItem('Diamond 1,2')
        self.Tearr5.addItem('Diamond 3,4')
        self.Tearr5.addItem('Platinum')
        self.Tearr5.addItem('Gold')
        self.Tearr5.addItem('Silver')
        self.Tearr5.addItem('Bronze')
        self.Tearr5.addItem('Iorn')



    def BTeamScore(self):
        try:
            self.Btop = 0
            self.BJG = 0
            self.BMID = 0
            self.BAD = 0
            self.BSUP = 0
            self.Btop = int(self.Blabel1.text())
            self.BJG = int(self.Blabel2.text())
            self.BMID = int(self.Blabel3.text())
            self.BAD = int(self.Blabel4.text())
            self.BSUP = int(self.Blabel5.text())

            self.BTeamscore = (self.Btop + self.BJG + self.BMID + self.BAD + self.BSUP)
            self.Blabel.setText(str(self.BTeamscore))
            self.Blabel.repaint()
        except:
            pass

    def RTeamScore(self):
        try:
            self.Rtop = 0
            self.RJG = 0
            self.RMID = 0
            self.RAD = 0
            self.RSUP = 0
            self.Rtop = int(self.Rlabel1.text())
            self.RJG = int(self.Rlabel2.text())
            self.RMID = int(self.Rlabel3.text())
            self.RAD = int(self.Rlabel4.text())
            self.RSUP = int(self.Rlabel5.text())

            self.RTeamscore = (self.Rtop + self.RJG + self.RMID + self.RAD + self.RSUP)
            self.Rlabel.setText(str(self.RTeamscore))
            self.Rlabel.repaint()
        except:
            pass

    def Win(self):
        self.Rscore = int(self.Rlabel.text())
        self.Bscore = int(self.Blabel.text())
        if self.Rscore == self.Bscore:
            self.Wlabel.setText('  양팀 비등')
            self.Wlabel.repaint()
        else:
            if self.Rscore > self.Bscore:
                self.Wlabel.setText('레드팀 우세')
                self.Wlabel.repaint()
            else:
                self.Wlabel.setText('블루팀 우세')
                self.Wlabel.repaint()



    # def Reset(self):
    #     self.delete.toggle()
    #     with con:
    #         cur = con.cursor()
    #         cur.execute("DELETE FROM Data WHERE Score < 99999")
    #         con.commit()
    #         self.Table.clear()
    #         column_headers = ['NickName', 'Tear', 'Line', 'Score']
    #         self.Table.setHorizontalHeaderLabels(column_headers)

    # def setTableWidgetData(self):
    #     column_headers = ['NickName', 'Tear', 'Line', 'Score']
    #     self.Table.setHorizontalHeaderLabels(column_headers)
    #     cur.execute("select Nick,Tear,Line,Score from Data where Score < 999999")
    #     self.full = cur.fetchall()
    #     for i in range(len(self.full)):
    #         self.full2 = self.full[i]
    #         for j in range(len(self.full2)):
    #             self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #             self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #             self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #             self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))

    # def NickS(self, text):
    #     self.Nick1 = text

    # def TearS(self, text):
    #     self.Tear1 = text

    # def LineS(self, text):
    #     self.Line1 = text

    def Score1(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[0]
            print(self.score2)
            self.Blabel1.setText(self.score2)
            self.Blabel1.repaint()

    def Score2(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[1]
            print(self.score2)
            self.Blabel2.setText(self.score2)
            self.Blabel2.repaint()

    def Score3(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[2]
            print(self.score2)
            self.Blabel3.setText(self.score2)
            self.Blabel3.repaint()

    def Score4(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[3]
            print(self.score2)
            self.Blabel4.setText(self.score2)
            self.Blabel4.repaint()

    def Score5(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[4]
            print(self.score2)
            self.Blabel5.setText(self.score2)
            self.Blabel5.repaint()

    def Score6(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[0]
            print(self.score2)
            self.Rlabel1.setText(self.score2)
            self.Rlabel1.repaint()

    def Score7(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[1]
            print(self.score2)
            self.Rlabel2.setText(self.score2)
            self.Rlabel2.repaint()

    def Score8(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[2]
            print(self.score2)
            self.Rlabel3.setText(self.score2)
            self.Rlabel3.repaint()

    def Score9(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[3]
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[3]
            print(self.score2)
            self.Rlabel4.setText(self.score2)
            self.Rlabel4.repaint()

    def Score10(self, value):
        if value == 1:
            self.score1 = self.chll
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 2:
            self.score1 = self.grm
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 3:
            self.score1 = self.master
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 4:
            self.score1 = self.D12
            self.score2 = self.score1[4]
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 5:
            self.score1 = self.D34
            self.score2 = self.score1[4]
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 6:
            self.score1 = self.pla
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 7:
            self.score1 = self.gld
            self.score2 = self.score1[4]
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 8:
            self.score1 = self.slv
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 9:
            self.score1 = self.blz
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()
        if value == 10:
            self.score1 = self.iorn
            self.score2 = self.score1[4]
            print(self.score2)
            self.Rlabel5.setText(self.score2)
            self.Rlabel5.repaint()

    # def Score2(self, value):
    #     if value == 1:
    #         self.score2 = self.score1[0]
    #     if value == 2:
    #         self.score2 = self.score1[1]
    #     if value == 3:
    #         self.score2 = self.score1[2]
    #     if value == 4:
    #         self.score2 = self.score1[3]
    #     if value == 5:
    #         self.score2 = self.score1[4]
    #
    # def SaveS(self):
    #     try:
    #         con = sqlite3.connect("Tournament Data.db")
    #         cur = con.cursor()
    #         cur.execute('''INSERT INTO Data VALUES (:Nick, :Tear, :Line, :Score)''',
    #                 {"Nick": self.Nick1, "Tear": self.Tear1, "Line": self.Line1, "Score": self.score2})
    #         con.commit()
    #         with con:
    #             with open('Tournament Data Backup File.sql', 'w') as f:
    #                 for line in con.iterdump():
    #                     f.write('%s\n' % line)
    #                 print('Save Completed')
    #         self.save.toggle()
    #         cur.execute("select Nick,Tear,Line,Score from Data where Score < 999999")
    #         self.full = cur.fetchall()
    #         for i in range(len(self.full)):
    #             self.full2 = self.full[i]
    #             for j in range(len(self.full2)):
    #                 self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #                 self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #                 self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #                 self.Table.setItem(i, j, QTableWidgetItem(self.full2[j]))
    #                 self.Tear.clear()
    #                 self.Tear.addItem('Tear')
    #                 self.Tear.addItem('Challenger')
    #                 self.Tear.addItem('GrandMaster')
    #                 self.Tear.addItem('Master')
    #                 self.Tear.addItem('Diamond 1,2')
    #                 self.Tear.addItem('Diamond 3,4')
    #                 self.Tear.addItem('Platinum')
    #                 self.Tear.addItem('Gold')
    #                 self.Tear.addItem('Silver')
    #                 self.Tear.addItem('Bronze')
    #                 self.Tear.addItem('Iorn')
    #                 self.Line.clear()
    #                 self.Line.addItem('Line')
    #                 self.Line.addItem('TOP')
    #                 self.Line.addItem('JG')
    #                 self.Line.addItem('MID')
    #                 self.Line.addItem('AD')
    #                 self.Line.addItem('SUP')
    #                 self.Nick.clear()
    #     except:
    #         self.save.toggle()
    #         pass


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())