import sys
from PySide6.QtWidgets import *
app = QApplication(sys.argv)
win = QWidget()
win.resize(320, 240) #กาํหนดขนาดของหนา้ตา่ งโปรแกรม
win.setWindowTitle("Hello, World!") #กาํหนดชืÉอตรงหัวโปรแกรม
layout = QVBoxLayout() #ดึง QVBoxLayout() มาใชง้านเพิÉมให้เราสามารถดึงวตัถุมารวมกนั ได้
win.setLayout(layout) #กาํหนดให้ตวัแปร win ชึÉงเป็ น QWidget ดึงตวัแปรทีÉอยใู่ น layout มาแสดง
label = QLabel("Hello World") #กาํหนดขอ้ความ
layout.addWidget(label) #เพิÉมดึงตวัแปร label เขา้มา
win.show() #แสดง
app.exec()
sys.exit()