import sys
import random

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QPushButton, QRadioButton,
                             QApplication, QDesktopWidget, QLabel)



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.cnt = 0
        self.txt = 'aa'
        self.labList = []
        self.labTop=130
        datetime = QDateTime.currentDateTime()
        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(1, 10)
        self.sld.setSingleStep(1)
        self.sld.setTickPosition(QSlider.TicksBelow)

        self.rbtn1 = QRadioButton('Lotto 6 aus 49', self)

        self.rbtn2 = QRadioButton(self)
        self.rbtn2.setText('Euro Jackpot')
        self.rbtn2.setChecked(True)

        self.btn1 = QPushButton('RUN', self)

        self.lbl1 = QLabel("How many?", self)
        self.lbl1.move(10, 10)
        self.lcd.move(10, self.lbl1.height())
        self.sld.move(10, self.lbl1.height() + self.lcd.height())
        self.lbl2 = QLabel('|', self)
        self.lbl3 = QLabel('|', self)
        self.lbl2.move(self.lcd.width(), self.lbl1.height())
        self.lbl3.move(self.sld.width(), self.lbl1.height() + self.lcd.height())
        self.lbl4 = QLabel("Which Lottery?",self)
        self.lbl4.move(115,10)
        self.rbtn1.move(115, self.lbl4.height())
        self.rbtn2.move(115, self.lbl4.height() + self.rbtn1.height())
        self.btn1.move(10, self.lbl1.height() + self.lcd.height() + self.sld.height())
        self.rbtn1.toggle()
        self.rbtn2.toggle()

        self.sld.valueChanged.connect(self.lcd.display)
        self.btn1.clicked.connect(self.buttonClicked)
        self.setGeometry(2000, 300, 300, 300)
        self.setWindowIcon(QIcon('logo\web.png'))
        self.setWindowTitle('Let win!!!')
        self.center()
        self.show()


    def buttonClicked(self):
        self.cnt = int(self.sld.value())
        self.lab = QLabel(str(self.cnt)+"are picked",self)
        self.lab.move(10, self.labTop)
        self.lab.show()


        if self.rbtn1.isChecked():
            self.txt = self.rbtn1.text()
            self.lab1 = QLabel(self.txt+ "ㄱㄱ", self)
            self.lab1.move(10, self.labTop+20)
            self.lab1.show()
            for i in range(0,self.cnt):
                lotto = random.sample(range(1, 49), 6)
                lotto.sort()
                bonus_number = random.sample(range(0, 9), 1)
                bonus_number.sort()
                self.labList.append(QLabel(str(lotto) + '    Losnummer: '+ str(bonus_number), self))
                self.labList[i].move(10, self.labTop+50 + (i*20))
                self.labList[i].show()
        else:
            self.txt = self.rbtn2.text()
            self.lab1 = QLabel(self.txt+ "ㄱㄱ", self)
            self.lab1.move(10, self.labTop+20)
            self.lab1.show()
            for i in range(0,self.cnt):
                Euro_jackpot = random.sample(range(1, 50), 5)
                Euro_jackpot.sort()
                lucky_number = random.sample(range(1, 10), 2)
                lucky_number.sort()
                self.labList.append(QLabel(str(Euro_jackpot) + '    Lucky number: ' + str(lucky_number), self))
                self.labList[i].move(10, self.labTop+50 + (i*20))
                self.labList[i].show()





    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
