#!/usr/bin/env python

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QScrollArea, QStatusBar, QPushButton
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit
from PySide6.QtGui import QShortcut, QKeySequence, QColor
from PySide6.QtCore import QTimer


import sys
from datetime import datetime
from patwlclass import PatWL

# need to do: pip install pyside6
# need to put patwlclass.py into site-packages directory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a shortcut to close the window when Esc is pressed
        shortcut = QShortcut(QKeySequence("Esc"), self)
        shortcut.activated.connect(self.close)

        self.setMinimumSize(1175, 700)
        curtime = datetime.now()
        self.setWindowTitle(f"Emergency email - {curtime:%m/%d/%Y %H:%M}")

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.showdefaultmessage()

        cssborder = "border: 1px solid gray;"

        mainlayout = QVBoxLayout()
        #tolayout = QHBoxLayout()
        #subjlayout = QHBoxLayout()

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainlayout)

        button = QPushButton("Email it!")
        button.setFixedSize(200, 50)
        button.setDefault(True)
        button.clicked.connect(self.button_clicked)
        button.setStyleSheet('background-color: lawngreen; border: 2px solid blue; border-radius: 20px')

        cbutton = QPushButton("Cancel")
        cbutton.setFixedSize(200, 50)
        cbutton.clicked.connect(self.cbutton_clicked)
        cbutton.setStyleSheet('background-color: #ff723a; border: 2px solid blue; border-radius: 20px')

        tolabel = QLabel("To:")
        self.toeb = QLineEdit()
        self.toeb.setStyleSheet(cssborder)

        subjlabel = QLabel("Subject:")
        self.subjeb = QLineEdit()
        self.subjeb.setStyleSheet(cssborder)

        msglabel = QLabel("Message:")
        self.editbox = QPlainTextEdit()
        self.editbox.setStyleSheet(cssborder)

        tohbox = QHBoxLayout()
        tohbox.addWidget(tolabel)
        tohbox.addWidget(self.toeb)

        subjhbox = QHBoxLayout()
        subjhbox.addWidget(subjlabel)
        subjhbox.addWidget(self.subjeb)

        buttonhbox = QHBoxLayout()
        buttonhbox.addWidget(cbutton)
        buttonhbox.addWidget(button)

        mainlayout.addLayout(tohbox)
        mainlayout.addLayout(subjhbox)
        mainlayout.addWidget(msglabel)
        mainlayout.addWidget(self.editbox)
        mainlayout.addLayout(buttonhbox)

        self.reseteb()

    def showdefaultmessage(self):
        self.status_bar.showMessage("Ready")

    def button_clicked(self):
        to = self.toeb.text()
        subj = self.subjeb.text()
        message = self.editbox.toPlainText()
        message += """


----------
This is an amateur radio email provided by the Jackson County Amateur Radio Association, in
Jackson County, MS on behalf of the sender. for more information see: https://JCMSARA.org

Please do not reply to this email.
"""
        #print(f"to: {to}, subj: {subj}, msg: {message}")

        pwl = PatWL()
        pwl.save(to, subj, message)

        self.status_bar.showMessage(f"Message sent to: {to}", 1500)

        self.reseteb()
        curtime = datetime.now()
        self.setWindowTitle(f"Emergency email - {curtime:%m/%d/%Y %H:%M}")
        QTimer.singleShot(2000, self.showdefaultmessage)

    def cbutton_clicked(self):
        self.reseteb()

    def reseteb(self):
        self.editbox.setPlainText("")
        self.subjeb.setText("Status of: ")
        self.toeb.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
    
