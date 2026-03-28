import sqlite3

from .teacher import Teacher


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.create_database()

    def create_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    faculty TEXT NOT NULL,
                    department TEXT NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    middle_name TEXT,
                    academic_title TEXT NOT NULL,
                    academic_degree TEXT NOT NULL,
                    work_experience REAL NOT NULL
                )
            """)

            conn.commit()

    def add_teacher(self, teacher: Teacher):
        with sqlite3.connect(f"{self.db_name}") as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                    INSERT INTO teachers (faculty, deprtment_name, fio, academic_title, academic_degree, work_experience)
                    VALUES(?, ?, ?, ?, ?, ?)
                    """,
                (
                    teacher.faculty,
                    teacher.department,
                    teacher.first_name,
                    teacher.last_name,
                    teacher.middle_name,
                    teacher.academic_title,
                    teacher.academic_degree,
                    teacher.work_experience,
                ),
            )

            conn.commit()

    def get_all_faculties(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT faculty FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_deprtments(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT department FROM teachers")
            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_academic_titles(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT academic_title FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_academic_degres(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT academic_degree FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_teachers_page(self, page_id: int, page_size: int):
        offset = (page_id - 1) * page_size
        with sqlite3.connect(f"{self.db_name}") as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM teachers LIMIT ? OFFSET ?", (page_size, offset)
            )
            rows = cursor.fetchall()
            return [Teacher.get_teacher_from_row(row) for row in rows]

    def get_teachers_by_name(self, first_name: str):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()

            cursor.execute("SELECT * FROM teachers WHERE first_name = ?", (first_name,))
            rows = cursor.fetchall()
            return [Teacher.get_teacher_from_row(row) for row in rows]

    def get_records_count(self) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM teachers")
            return cursor.fetchone()[0]
