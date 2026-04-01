from dataclasses import asdict
from xml.sax import make_parser

from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from src import config
from src.model.database import Database
from src.model.teacher import Teacher
from src.model.xml_reader import SAXParser
from src.model.xml_writer import DOMParser
from src.view.addition_window import AdditionWindow
from src.view.delete_window import DeleteWindow
from src.view.main_window import MainWindow
from src.view.search_window import SearchWindow


class Controller:
    def __init__(self, view: MainWindow, db: Database):
        self.db = db
        self.view = view

        self._connect()
        self.read_xml()
        self.update_display()

    def _connect(self):
        self.view.paginator.page_changed.connect(self.update_display)
        self.view.addition_action.triggered.connect(self.show_add_dialog)
        self.view.search_action.triggered.connect(self.show_search_dialog)
        self.view.delete_action.triggered.connect(self.show_delete_dialog)
        self.view.import_from_xml.triggered.connect(self.read_xml)
        self.view.export_into_xml.triggered.connect(self.write_xml)
        self.view.table_view.triggered.connect(
            lambda: self.view.view_stack.setCurrentIndex(0)
        )
        self.view.tree_view.triggered.connect(
            lambda: self.view.view_stack.setCurrentIndex(1)
        )

    def read_xml(self):
        path, _ = QFileDialog.getOpenFileName(
            self.view, "Открыть XMl", "", "XML files (*.xml)"
        )
        if path:
            try:
                self.db.drop_table()
                parser = make_parser()
                sax_handler = SAXParser()
                parser.setContentHandler(sax_handler)
                parser.parse(config.TEACHER_XML_PATH)

                teachers = sax_handler.teachers
                for teacher in teachers:
                    self.db.add_teacher(teacher)

                QMessageBox.information(self.view, "Успех", "Файл успешно импортирован")
            except Exception as e:
                QMessageBox.critical(
                    self.view, "Ошибка", f"Не удалось импортировать: {e}"
                )

    def write_xml(self):
        path, _ = QFileDialog.getSaveFileName(
            self.view, "Сохранить XML", "", "XML files (*.xml)"
        )
        print(path)
        if path:
            try:
                parser = DOMParser()
                teachers = self.db.get_all_teachers()
                parser.parse_doc(teachers, config.TEACHER_XML_PATH)
                QMessageBox.information(self.view, "Успех", f"Даныне сохранены")
            except Exception as e:
                QMessageBox.critical(self.view, "Ошибка", f"Не удалось сохранить: {e}")

    def update_display(self):
        limit, offset = self.view.paginator.get_limit_offset()
        teachers_page = self.db.get_teachers_page(limit, offset)
        total_records = self.db.get_records_count()
        self.view.table.update_table(teachers_page)
        self.view.update_tree(teachers_page)
        self.view.paginator.update_values(total_records)

    def show_add_dialog(self):
        self.add_dialog = AdditionWindow()
        if self.add_dialog.exec():
            data = self.add_dialog.get_data()
            self.db.add_teacher(Teacher(**data))
            self.update_display()

    def show_search_dialog(self):
        self.search_dialog = SearchWindow(self.view)

        faculties = self.db.get_all_faculties()
        departments = self.db.get_all_deprtments()
        academic_titles = self.db.get_all_academic_titles()
        academic_degrees = self.db.get_all_academic_degres()

        self.search_dialog.set_all_possible_values(
            faculties, departments, academic_titles, academic_degrees
        )

        def refresh_table():
            faculty = self.search_dialog.faculty_name.currentText()
            department = self.search_dialog.department_name.currentText()
            fio = self.search_dialog.fio.text()
            academic_title = self.search_dialog.academic_title.currentText()
            academic_degree = self.search_dialog.academic_degree.currentText()
            limit, offset = self.search_dialog.paginator.get_limit_offset()

            total_records, teachers = self.db.search_teachers(
                faculty, department, fio, academic_title, academic_degree, limit, offset
            )
            self.search_dialog.paginator.update_values(total_records)
            self.search_dialog.table.setRowCount(len(teachers))
            for row_idx, row in enumerate(teachers):
                for col_idx, (key, value) in enumerate(asdict(row).items()):
                    self.search_dialog.table.setItem(
                        row_idx, col_idx, QTableWidgetItem(str(value))
                    )

        self.search_dialog.search_button.clicked.connect(
            lambda: (
                setattr(self.search_dialog.paginator, "curr_page", 1),
                refresh_table(),
            )
        )
        self.search_dialog.paginator.page_changed.connect(refresh_table)
        self.search_dialog.exec()

    def show_delete_dialog(self):
        self.delete_dialog = DeleteWindow(self.view)

        faculties = self.db.get_all_faculties()
        departments = self.db.get_all_deprtments()
        academic_titles = self.db.get_all_academic_titles()
        academic_degrees = self.db.get_all_academic_degres()

        self.delete_dialog.set_all_possible_values(
            faculties, departments, academic_titles, academic_degrees
        )

        def refresh_preview():
            faculty = self.delete_dialog.faculty_name.currentText()
            department = self.delete_dialog.department_name.currentText()
            fio = self.delete_dialog.fio.text()
            academic_title = self.delete_dialog.academic_title.currentText()
            academic_degree = self.delete_dialog.academic_degree.currentText()
            limit, offset = self.delete_dialog.paginator.get_limit_offset()

            total_records, teachers = self.db.search_teachers(
                faculty, department, fio, academic_title, academic_degree, limit, offset
            )
            self.delete_dialog.paginator.update_values(total_records)
            self.delete_dialog.table.setRowCount(len(teachers))
            for row_idx, row in enumerate(teachers):
                for col_idx, (key, value) in enumerate(asdict(row).items()):
                    self.delete_dialog.table.setItem(
                        row_idx, col_idx, QTableWidgetItem(str(value))
                    )

        def delete():
            faculty = self.delete_dialog.faculty_name.currentText()
            department = self.delete_dialog.department_name.currentText()
            fio = self.delete_dialog.fio.text()
            academic_title = self.delete_dialog.academic_title.currentText()
            academic_degree = self.delete_dialog.academic_degree.currentText()

            count = self.db.delete_teachers(
                faculty, department, fio, academic_title, academic_degree
            )

            QMessageBox.information(
                self.delete_dialog, "Успех", f"Удалено: {count} записей"
            )

        self.delete_dialog.delete_button.clicked.connect(
            lambda: (
                setattr(self.delete_dialog.paginator, "curr_page", 1),
                refresh_preview(),
            )
        )
        self.delete_dialog.paginator.page_changed.connect(refresh_preview)
        self.delete_dialog.confirm_delete.clicked.connect(delete)
        self.delete_dialog.exec()
