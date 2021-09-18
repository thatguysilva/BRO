import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#setup the path of the Tor browser in your PC
tor_path = r"C:\Users\User\Desktop\Tor Browser\Browser\firefox.exe"
webbrowser.register("tor", None, webbrowser.BackgroundBrowser(tor_path))

class BroBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(BroBrowser, self).__init__(*args,**kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("BRO")
        self.window.setWindowIcon(QIcon("bro-icon.png"))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.reload_btn = QPushButton("⟳")
        self.reload_btn.setMinimumHeight(30)
        self.reload_btn.setMaximumWidth(25)
        self.reload_btn.setStyleSheet("background-color: #89CFF0")


        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(25)
        self.url_bar.setPlaceholderText("http://")

        self.go_btn = QPushButton("Let's surf!")
        self.go_btn.setMinimumHeight(30)

        self.tor_btn = QPushButton(" Switch to Tor")
        self.tor_btn.setMinimumHeight(30)
        self.tor_btn.setIcon(QIcon("tor1.jpg"))

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setMaximumWidth(15)
        self.back_btn.setStyleSheet("background-color: #eb576a")

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setMaximumWidth(15)
        self.forward_btn.setStyleSheet("background-color: #eb576a")

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.tor_btn)
        
        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.tor_btn.clicked.connect(lambda: webbrowser.get("tor").open(" "))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.reload_btn.clicked.connect(self.browser.reload)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://chickenonaraft.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))



            

app = QApplication([])
window = BroBrowser()
app.exec_()
