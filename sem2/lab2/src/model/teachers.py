import sqlite3

from .teacher import Teacher


class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.create_database()
        
    def create_database(self):
        with sqlite3.connect(f'{self.db_name}') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    faculty TEXT NOT NULL,
                    department_name TEXT NOT NULL,
                    fio TEXT NOT NULL,
                    academic_title TEXT NOT NULL,
                    academic_degree TEXT NOT NULL,
                    work_expirience REAL NOT NULL,
                )
            """)
            
            conn.commit()
            
    def add_teacher(self, teacher: Teacher):
        with sqlite3.connect(f'{self.db_name}') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                    INSERT INTO teachers (faculty, deprtment_name, fio, academic_title, academic_degree, work_expirience)
                    VALUES(?, ?, ?, ?, ?, ?)
                    """, (teacher.faculty, teacher.department_name, teacher.fio, teacher.academic_title, teacher.academic_degree, teacher.work_expirience))
            
            conn.commit()
            
    def get_all_teachers(self):
        with sqlite3.connect(f'{self.db_name}') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                    SELECT * FROM teachers
                """)
    def selecet_teacher(self):
        pass
        