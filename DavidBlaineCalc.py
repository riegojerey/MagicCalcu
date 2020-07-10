from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("David Blaine Calculator")
        self.UI()
        
    def UI(self):
        ###label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("ano na boiiii")
        self.label.move(100,100)
        ###button
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("1")
        self.button1.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        self.updatewidth()
        
    def updatewidth(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
window()