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


class SearchWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Найти учителей")
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

        self.search_button = QPushButton("Найти записи")
        self.search_button.setFixedHeight(40)

        layout.addWidget(self.search_button)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            [
                "Факультет",
                "Кафедра",
                "ФИО",
                "Ученое звание",
                "Ученая степень",
                "Стаж работы",
            ]
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.paginator = Pagination()

        layout.addWidget(self.table)
        layout.addWidget(self.paginator)

    def set_all_possible_values(
        self, faculties, departments, academic_titles, academic_degrees
    ):
        self.faculty_name.addItems([""] + faculties)
        self.department_name.addItems([""] + departments)
        self.academic_title.addItems([""] + academic_titles)
        self.academic_degree.addItems([""] + academic_degrees)

    def update_table(self, teachers: list[Teacher]) -> None:
        self.table.setRowCount(len(teachers))
        for row_idx, row in enumerate(teachers):
            for col_idx, (key, value) in enumerate(asdict(row).items()):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
