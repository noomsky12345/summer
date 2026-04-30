import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

class myMessageBox(QWidget):
    def __init__(self):
        # ใช้ super().__init__() เป็นมาตรฐานที่แนะนำสำหรับ Python 3
        super().__init__()
        
        # กำหนดตำแหน่ง (x, y) และขนาด (กว้าง, สูง)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('กล่องข้อความ') 

    # ฟังก์ชันนี้จะทำงานอัตโนมัติเมื่อมีการพยายามปิดหน้าต่าง (เช่น กดปุ่ม X)
    def closeEvent(self, event):
        # สร้างกล่องถามคำถาม (Parent, หัวข้อ, ข้อความ, ปุ่มที่ต้องการให้มี)
        reply = QMessageBox.question(self, 'ยืนยันการปิด',
                                   "คุณแน่ใจนะว่าต้องการปิดโปรแกรม?", 
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            print("ผู้ใช้ยืนยัน: ปิดโปรแกรม")
            event.accept()  # ยืนยันให้ปิดโปรแกรมได้
        else:
            print("ผู้ใช้ยกเลิก: โปรแกรมทำงานต่อ")
            event.ignore()  # สั่งให้เพิกเฉยต่อการกดปิด (หน้าต่างจะไม่ถูกปิด)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = myMessageBox()
    qb.show()
    sys.exit(app.exec())