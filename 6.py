import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        # กำหนดขนาดหน้าต่าง
        self.resize(600, 400)
        self.setWindowTitle("HTML Content Test")
        
        # เขียน HTML โค้ดลงในตัวแปร String
        # (ลบข้อความส่วนเกินจากเอกสาร OOP ออกให้แล้วครับ)
        html_content = """
        <html>
        <head>
            <meta charset="utf-8">
            <title>ทดสอบ</title>
            <style>
                body { font-family: 'Tahoma', sans-serif; background-color: #f0f0f0; }
                h1 { color: #2c3e50; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <hr />
            <p>ทดสอบการแสดงผล HTML ใน QWebEngineView</p>
            <p style="color: blue;">ยินดีด้วย! คุณกำลังรัน HTML บน Python</p>
        </body>
        </html>
        """
        
        # สั่งให้ WebEngine แสดงผล HTML
        self.setHtml(html_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())