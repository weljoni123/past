import sys
import pyautogui
import pyperclip
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 230)
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setText("Copy-Paste Tool")

        self.countdown_label = QtWidgets.QLabel(self.centralwidget)
        self.countdown_label.setGeometry(QtCore.QRect(50, 70, 200, 30))
        self.countdown_label.setObjectName("countdown_label")
        self.countdown_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.countdown_label.setText("")
        self.get_xpath_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_xpath_button.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.get_xpath_button.setObjectName("get_xpath_button")
        self.get_xpath_button.setText("Get XPath")
        self.get_xpath_button.clicked.connect(self.get_xpath)
        self.paste_button = QtWidgets.QPushButton(self.centralwidget)
        self.paste_button.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.paste_button.setObjectName("paste_button")
        self.paste_button.setText("Paste")
        self.paste_button.clicked.connect(self.paste_text)

        self.author_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.author_textbox.setGeometry(QtCore.QRect(50, 180, 200, 20))
        self.author_textbox.setObjectName("author_textbox")
        self.author_textbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.author_textbox.setText("weljoni")
        self.author_textbox.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.get_xpath_button.setText(_translate("MainWindow", "Get XPath"))
        self.paste_button.setText(_translate("MainWindow", "Paste"))

    def get_xpath(self):
        message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information,
                                            "Get XPath", "Please select a position and copy XPath.")
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        message_box.exec()

    def paste_text(self):
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            self.countdown_label.setText("Pasting in 5 seconds")
            QtCore.QTimer.singleShot(5000, lambda: pyautogui.typewrite(clipboard_content, interval=0.1))  # Paste clipboard content after 5 seconds

    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())









