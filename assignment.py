import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class Tulisan(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Week 6")
        self.setGeometry(100, 100, 600, 300)

        self.nim = "F1D022102"
        self.nama = "Yusril Ibtida Ramdhani"

        self.lanNIM = QLabel(self.nim, self)
        self.lanNIM.setAlignment(Qt.AlignCenter)
        self.lanNIM.setFont(QFont("Arial", 30))
        self.lanNIM.setAutoFillBackground(True)

        self.labNama = QLabel(f"Created by: {self.nama} | {self.nim}")
        self.labNama.setAlignment(Qt.AlignCenter)
        self.labNama.setFont(QFont("Arial", 10))

        self.sizeSlider = self.slider(20, 60, self.changeSize)
        self.bgColor = self.slider(0, 255, self.changeBgColor)
        self.fontColor = self.slider(0, 255, self.changeFontColor)

        layout = QVBoxLayout()
        layout.addWidget(self.lanNIM)
        layout.addLayout(self.makeSlider("Ukuran Font", self.sizeSlider))
        layout.addLayout(self.makeSlider("Warna Latar", self.bgColor))
        layout.addLayout(self.makeSlider("Warna Font", self.fontColor))
        layout.addWidget(self.labNama)
        self.setLayout(layout)

        self.changeSize()
        self.changeBgColor()
        self.changeFontColor()

    def slider(self, min_val, max_val, fungsi):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(min_val, max_val)
        slider.setValue((min_val + max_val) // 2)
        slider.valueChanged.connect(fungsi)
        return slider

    def makeSlider(self, judul, slider):
        label_judul = QLabel(judul)
        label_judul.setFixedWidth(100)
        baris = QHBoxLayout()
        baris.addWidget(label_judul)
        baris.addWidget(slider)
        return baris

    def changeSize(self):
        ukuran = self.sizeSlider.value()
        font = self.lanNIM.font()
        font.setPointSize(ukuran)
        self.lanNIM.setFont(font)

    def changeBgColor(self):
        nilai = self.bgColor.value()
        warna = QColor(nilai, nilai, nilai)
        palet = self.lanNIM.palette()
        palet.setColor(QPalette.Window, warna)
        self.lanNIM.setPalette(palet)

    def changeFontColor(self):
        nilai = self.fontColor.value()
        warna = QColor(nilai, nilai, nilai)
        palet = self.lanNIM.palette()
        palet.setColor(QPalette.WindowText, warna)
        self.lanNIM.setPalette(palet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tulisan()
    window.show()
    sys.exit(app.exec_())
