import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. กำหนดขนาดหน้าต่างและชื่อโปรแกรม
        self.resize(320, 240) 
        self.setWindowTitle("Hello, World!") 
        
        # 2. สร้าง Layout สำหรับจัดวางปุ่ม
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 3. สร้างปุ่มกด (QPushButton)
        hello_btn = QPushButton("Hello world!") 
        
        # ทริค: เมื่อใช้ Layout ตัว Layout จะพยายามขยายปุ่มให้เต็มพื้นที่
        # หากต้องการคุมขนาดปุ่มให้คงที่ แนะนำให้ใช้ setFixedSize แทนครับ
        hello_btn.setFixedSize(100, 30) 
        
        # 4. เพิ่มปุ่มเข้าไปใน Layout
        layout.addWidget(hello_btn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())