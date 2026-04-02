
from PyQt6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class AdditionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить учителя")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.faculty = QLineEdit()
        self.department = QLineEdit()
        self.fio = QLineEdit()
        self.academic_title = QLineEdit()
        self.academic_degree = QLineEdit()
        self.work_experience = QLineEdit()

        form.addRow("Факультет:", self.faculty)
        form.addRow("Кафедра:", self.department)
        form.addRow("ФИО:", self.fio)
        form.addRow("Ученое звание:", self.academic_title)
        form.addRow("Ученая степень:", self.academic_degree)
        form.addRow("Опыт работы:", self.work_experience)

        layout.addLayout(form)

        buttons = QHBoxLayout()
        save_button = QPushButton("Сохранить")
        reject_button = QPushButton("Отменить")
        buttons.addWidget(save_button)
        buttons.addWidget(reject_button)

        save_button.clicked.connect(self.accept_push)
        reject_button.clicked.connect(self.reject_push)

        layout.addLayout(buttons)

    def reject_push(self):
        self.reject()

    def accept_push(self):
        self.accept()

    def get_data(self):
        return {
            "faculty": self.faculty.text(),
            "department": self.department.text(),
            "fio": self.fio.text(),
            "academic_title": self.academic_title.text(),
            "academic_degree": self.academic_degree.text(),
            "work_experience": self.work_experience.text(),
        }
