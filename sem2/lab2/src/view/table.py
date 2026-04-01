from dataclasses import asdict

from PyQt6.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget
from src.model.teacher import Teacher


class Table(QTableWidget):
    def __init__(self, labels: list[str], parent: QWidget = None):
        super().__init__(parent=parent)

        self.setColumnCount(len(labels))
        self.setHorizontalHeaderLabels(labels)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def update_table(self, teachers: list[Teacher]) -> None:
        self.setRowCount(len(teachers))
        for row_idx, row in enumerate(teachers):
            for col_idx, (_, value) in enumerate(asdict(row).items()):
                self.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
