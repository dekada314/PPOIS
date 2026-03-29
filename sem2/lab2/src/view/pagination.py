import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTableWidget,
    QTreeWidget,
    QVBoxLayout,
    QWidget,
)


class Pagination(QWidget):
    page_changed = pyqtSignal(str)
    page_size_changed = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        
        self.curr_page = 1
        self.page_size = 10
        self.total_records = 0
        self.total_pages = 1
        
        layout = QHBoxLayout(self)
        layout.addWidget(QLabel("Записей на стр:"))
        
        self.page_size_changer = QComboBox()
        self.page_size_changer.addItems(["5", "10", "20", "50"])
        self.page_size_changer.setCurrentText(str(self.page_size))
        self.page_size_changer.currentTextChanged.connect(self.update_page_size)
        
        layout.addWidget(self.page_size_changer)
        
        layout.addSpacerItem(QSpacerItem(15, 10, QSizePolicy.Policy.Expanding))


        self.to_first_page = QPushButton("<<")
        self.to_prev_page = QPushButton("<")
        self.page_info = QLabel(f"Страница 1 из 1")
        self.to_next_page = QPushButton(">")
        self.to_last_page = QPushButton(">>")
        
        layout.addWidget(self.to_first_page)
        layout.addWidget(self.to_prev_page)
        layout.addWidget(self.page_info)
        layout.addWidget(self.to_next_page)
        layout.addWidget(self.to_last_page)
        
        layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding))
        
        self.total_info = QLabel(f"Всего записей: {self.total_pages}")
        
        self.to_first_page.clicked.connect(self.go_to_first_page)
        self.to_prev_page.clicked.connect(self.go_to_prev_page)
        self.to_next_page.clicked.connect(self.go_to_next_page)
        self.to_last_page.clicked.connect(self.go_to_last_page)
        
    def update_table(self):
        pass
    
    def update_page_size(self):
        self.curr_page = 1
        self.page_size_changed.emit()
    
    def go_to_first_page(self):
        if self.curr_page != 1:
            self.curr_page = 1
            self.page_changed.emit()   
             
    def go_to_prev_page(self):
        if self.curr_page > 1:
            self.curr_page -= 1
            self.page_changed.emit()   
             
    def go_to_next_page(self):
        if self.curr_page < self.total_pages:
            self.curr_page += 1
            self.page_changed.emit()
                
    def go_to_last_page(self):
        if self.curr_page != self.total_pages:
            self.curr_page = self.total_pages
            self.page_changed.emit()    
            
    def get_limit_offset(self):
        limit = self.page_size
        offset = (self.curr_page - 1) * self.page_size
        return (limit, offset)