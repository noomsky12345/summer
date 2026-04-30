# Import PySide6 classes
import sys
from PySide6.QtWidgets import *
# สร้างโปรแกรมดว้ย Qt
app = QApplication(sys.argv)
# สร้าง Label และแสดง
label = QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec()
sys.exit()