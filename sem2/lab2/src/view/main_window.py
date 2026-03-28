import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("легенда")
        self.resize(900, 600)
        
        self.label = QLabel("кликай", self)
        self.output = QLabel("ответ", self)
        self.counter_label = QLabel("0:", self)
        
        self.counter = 0
        
        self.button1 = QPushButton("Привет")
        self.button2 = QPushButton("Пока")
        self.button3 = QPushButton("Поднять счетчик")
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.output)
        layout.addWidget(self.counter_label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        
        self.setLayout(layout)

        
        self.button1.clicked.connect(self.say_hello)
        self.button2.clicked.connect(self.say_bye)
        self.button3.clicked.connect(self.increase_counter)
        
        
    def say_hello(self):
        self.output.setText("Привет!")
        
    def say_bye(self):
        self.output.setText("Пока!")
        
    def increase_counter(self):
        self.counter += 1
        self.counter_label.setText(str(self.counter))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())