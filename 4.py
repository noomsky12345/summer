import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. กำหนดขนาดหน้าต่างและชื่อโปรแกรม
        self.resize(320, 240) 
        self.setWindowTitle("Hello, World!") 
        
        # 2. สร้าง Layout สำหรับจัดเรียง Widget แนวตั้ง
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 3. สร้าง Widget ข้อความ (Label)
        label1 = QLabel("Hello World")
        label2 = QLabel("สวัสดี")
        label3 = QLabel("เพิ่งเริ่มต้นเรียน PySide -..- จากผู้เขียนบทความ")
        
        # 4. นำ Widget ใส่เข้าไปใน Layout (จะเรียงต่อกันจากบนลงล่าง)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())