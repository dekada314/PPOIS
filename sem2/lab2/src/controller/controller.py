from xml.sax import make_parser

from src import config
from src.model.database import Database
from src.model.xml_reader import SAXParser
from src.view.main_window import MainWindow


class Controller:
    def __init__(self, view: MainWindow, db: Database):
        self.db = db
        self.view = view
        
        self._connect()
        self.read_xml()
        self.update_display()
        
    def _connect(self):
        # self.view.addition_action.triggered.connect()
        # self.view.cha
        self.view.paginator.page_changed.connect(self.update_display)

    def read_xml(self):
        parser = make_parser()
        sax_handler = SAXParser()
        parser.setContentHandler(sax_handler) 
        parser.parse(config.TEACHER_XML_PATH)
        teachers =  sax_handler.teachers
        for teacher in teachers:
            self.db.add_teacher(teacher)
        
    def update_display(self):
        limit, offset = self.view.paginator.get_limit_offset()
        teachers_page = self.db.get_teachers_page(limit, offset)
        total_records = self.db.get_records_count()
        self.view.update_table(teachers_page)
        self.view.paginator.update_values(total_records)
        