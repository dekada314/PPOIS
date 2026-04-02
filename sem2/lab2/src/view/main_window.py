from dataclasses import asdict

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QHeaderView,
    QMainWindow,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
from src.model.teacher import Teacher
from src.view.pagination import Pagination
from src.view.table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учителя")
        self.resize(900, 600)

        main_widget = QWidget()
        self.layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        self.view_stack = QStackedWidget()
        labels = [
            "Факультет",
            "Кафедра",
            "ФИО",
            "Ученое звание",
            "Ученая степень",
            "Стаж работы",
        ]

        self.table = Table(labels)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Данные учителя"])

        self.view_stack.addWidget(self.table)
        self.view_stack.addWidget(self.tree)

        self.paginator = Pagination()

        self.layout.addWidget(self.view_stack)
        self.layout.addWidget(self.paginator)

        self._create_menu_bar()

    def set_tree_node(self, params: dict[str: str, str: dict[str: str]]) -> None:
        root = QTreeWidgetItem(self.tree, [params["root"]])
        for key, value in params["childrens"].items():
            QTreeWidgetItem(root, [f"{key}: {value}"])

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        operation_menu = menu_bar.addMenu("Операции")

        self.addition_action = QAction("Сохранение", self)
        self.delete_action = QAction("Удаление", self)
        self.search_action = QAction("Поиск", self)

        operation_menu.addAction(self.addition_action)
        operation_menu.addAction(self.delete_action)
        operation_menu.addAction(self.search_action)

        file_menu = menu_bar.addMenu("Файл")

        self.export_into_xml = QAction("Сохранить в xml", self)
        self.import_from_xml = QAction("Извлечь из xml", self)

        file_menu.addAction(self.export_into_xml)
        file_menu.addAction(self.import_from_xml)

        view_menu = menu_bar.addMenu("Вид")

        self.table_view = QAction("В виде таблицы", self)
        self.tree_view = QAction("В виде дерева", self)

        view_menu.addAction(self.table_view)
        view_menu.addAction(self.tree_view)
