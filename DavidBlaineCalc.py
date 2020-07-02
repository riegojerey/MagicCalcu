from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("David Blaine Calculator")
    
    
    label = QtWidgets.QLabel(win)
    label.setText("ano na boiiii")
    label.move(100,100)
    win.show()
    sys.exit(app.exec())

window()