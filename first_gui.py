# PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("habib1.JPG"))

        label=QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: gray;"
                            "background-color: violet;"
                            "font-weight: bold;"
                            "font-style: italic;" 
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignTop) #Vertically Top
        # label.setAlignment(Qt.AlignBottom) #Vertically Bottom
        # label.setAlignment(Qt.AlignCenter) #Vertically Center
        # label.setAlignment(Qt.AlignRight) #Horizontally Right
        # label.setAlignment(Qt.AlignLeft) #Horizontal Left
        # label.setAlignment(Qt.AlignHCenter) #Horizontally Center

        label.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    main()
