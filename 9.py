import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtGui import QFont

# 1. สร้าง Application
app = QApplication(sys.argv)

# 2. สร้างปุ่ม Quit
quit_btn = QPushButton("Quit")

# 3. กำหนดขนาดและฟอนต์
quit_btn.resize(75, 30)
# ปรับแก้การเรียก QFont.Bold ให้ถูกต้องตามหลัก PySide6
quit_btn.setFont(QFont("Times", 18, QFont.Weight.Bold))

# 4. การเชื่อมต่อ Signal & Slot (แบบใหม่)
# เมื่อ quit_btn ถูกคลิก (clicked) -> ให้ไปเรียกใช้คำสั่งปิดโปรแกรม (app.quit)
quit_btn.clicked.connect(app.quit)

# 5. แสดงผล
quit_btn.show()

# 6. รันโปรแกรม (ใน PySide6 ใช้ exec() แทน exec_() ได้เลยครับ)
sys.exit(app.exec())