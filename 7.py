import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        # กำหนดขนาดหน้าต่าง
        self.resize(500, 500)
        self.setWindowTitle("Display Image from Binary")

        try:
            # 1. เปิดไฟล์รูปภาพในโหมด 'rb' (Read Binary) และอ่านข้อมูลทั้งหมด
            with open('101_0336.png', 'rb') as f:
                img_data = f.read()
            
            # 2. นำข้อมูล Binary มาแสดงผล โดยระบุ MIME type เป็น "image/png"
            self.setContent(img_data, "image/png")
            
        except FileNotFoundError:
            # กรณีหาไฟล์รูปภาพไม่เจอ
            print("Error: ไม่พบไฟล์ 101_0336.png ในโฟลเดอร์เดียวกับโปรแกรม")
            self.setHtml("<h1>ไม่พบไฟล์รูปภาพ</h1>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())