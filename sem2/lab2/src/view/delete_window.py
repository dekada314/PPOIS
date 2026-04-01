import sys
import traceback
from dataclasses import asdict

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QVBoxLayout,
    QWidget,
)
from src.model.teacher import Teacher
from src.view.pagination import Pagination
from src.view.table import Table


class DeleteWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Удалить учителей")
        self.setFixedSize(1000, 700)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.fio = QLineEdit()
        self.fio.setPlaceholderText("ФИО или любая часть...")

        form.addRow("ФИО:", self.fio)

        self.work_experience = QLineEdit()
        self.work_experience.setPlaceholderText("Задайте диапозон(например 1-13)...")
        form.addRow("Стаж:", self.work_experience)

        layout.addLayout(form)

        self.department_name = QComboBox()
        self.department_name.setFixedSize(200, 50)
        layout.addWidget(self.department_name)

        self.faculty_name = QComboBox()
        self.faculty_name.setFixedSize(200, 50)
        layout.addWidget(self.faculty_name)

        self.academic_title = QComboBox()
        self.academic_title.setFixedSize(200, 50)
        layout.addWidget(self.academic_title)

        self.academic_degree = QComboBox()
        self.academic_degree.setFixedSize(200, 50)
        layout.addWidget(self.academic_degree)

        self.delete_button = QPushButton("Отобразить записи перед удалением")
        self.delete_button.setFixedHeight(40)

        layout.addWidget(self.delete_button)

        labels = [
            "Факультет",
            "Кафедра",
            "ФИО",
            "Ученое звание",
            "Ученая степень",
            "Стаж работы",
        ]
        self.table = Table(labels)

        self.paginator = Pagination()

        layout.addWidget(self.table)
        layout.addWidget(self.paginator)

        self.confirm_delete = QPushButton("ПОДТВЕРДИТЬ УДАЛЕНИЕ ВСЕХ НАЙДЕННЫХ ЗАПИСЕЙ")
        self.confirm_delete.setStyleSheet("""
            QPushButton { background-color: #f44336; color: white; font-weight: bold; padding: 10px; }
            QPushButton:disabled { background-color: #ef9a9a; }
        """)
        layout.addWidget(self.confirm_delete)

    def set_all_possible_values(
        self, faculties, departments, academic_titles, academic_degrees
    ):
        self.faculty_name.addItems([""] + faculties)
        self.department_name.addItems([""] + departments)
        self.academic_title.addItems([""] + academic_titles)
        self.academic_degree.addItems([""] + academic_degrees)
