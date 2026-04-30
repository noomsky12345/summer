import sys
from PySide6.QtWidgets import *
app = QApplication(sys.argv)
win = QWidget()
win.resize(320, 240) #กาํหนดขนาดของหนา้ตา่ งโปรแกรม
win.setWindowTitle("Hello, World!") #กาํหนดชืÉอตรงหัวโปรแกรม
win.show() #แสดง
app.exec()
sys.exit()