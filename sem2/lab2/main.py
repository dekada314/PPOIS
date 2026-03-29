import sys

from PyQt6.QtWidgets import QApplication
from src import config
from src.controller.controller import Controller
from src.model.database import Database
from src.view.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    db = Database(config.TEACHER_SQLITE3_PATH)
    controller = Controller(view, db)
    
    view.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()