import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        # กำหนดขนาดหน้าต่างเริ่มต้น
        self.resize(1024, 768)
        self.setWindowTitle("My Mini Browser")
        
        # ดึงหน้าเว็บเพจมาแสดง
        self.load(QUrl("http://www.google.co.th"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # สร้าง Object จากคลาสที่เรานิยามไว้
    web = myWeb()
    web.show()
    
    sys.exit(app.exec())