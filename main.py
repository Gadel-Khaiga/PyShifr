#!/usr/bin/python3.8
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

Form, Window = uic.loadUiType("cezar.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    a=form.input1.text()
    j=form.input2.text()

    count = []
    for c in a:
        count.append(ord(c))  # ID of word(UNICODE) /// X ///

    shifr = []
    for y in count[:]:
        io = (y + int(j))
        shifr.append(io)
    Nsh = []
    for u in shifr:
        Nsh.append(chr(u))
    nn=''.join(Nsh)
    rec = []
    for y in shifr[:]:
        io = (y - int(j))
        rec.append(io)
    Rashrif = []
    for u in rec:
        Rashrif.append(chr(u))
    rr=''.join(Rashrif)
    form.label.setText(f'{nn}')
    form.label_2.setText(f'{rr}')




form.pushButton.clicked.connect(on_click)

app.exec()
