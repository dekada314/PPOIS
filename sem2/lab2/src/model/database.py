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
                    fio TEXT NOT NULL,
                    academic_title TEXT NOT NULL,
                    academic_degree TEXT NOT NULL,
                    work_experience REAL NOT NULL
                )
            """)

            conn.commit()

    def add_teacher(self, teacher: Teacher):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                    INSERT INTO teachers (faculty, department, fio, academic_title, academic_degree, work_experience)
                    VALUES(?, ?, ?, ?, ?, ?)
                    """,
                (
                    teacher.faculty,
                    teacher.department,
                    teacher.fio,
                    teacher.academic_title,
                    teacher.academic_degree,
                    teacher.work_experience,
                ),
            )

            conn.commit()

    def get_all_faculties(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT DISTINCT faculty FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_deprtments(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT DISTINCT department FROM teachers")
            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_academic_titles(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT DISTINCT academic_title FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_all_academic_degres(self) -> list[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT DISTINCT academic_degree FROM teachers")

            rows = cursor.fetchall()
            return [row[0] for row in rows]

    def get_teachers_page(self, limit: int, offset: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM teachers LIMIT ? OFFSET ?", (limit, offset))
            rows = cursor.fetchall()
            return [Teacher.get_teacher_from_row(row) for row in rows]

    def get_records_count(self) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM teachers")
            return cursor.fetchone()[0]

    def get_all_teachers(self) -> list[Teacher]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM teachers")
            return [Teacher.get_teacher_from_row(row) for row in cursor.fetchall()]

    def drop_table(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("DELETE FROM teachers")
            conn.commit()

    def _build_search_dongition(
        self, faculty, department, fio, academic_title, academic_degree
    ):
        sub_query = []
        params = []

        criteries = [
            "faculty",
            "department",
            "fio",
            "academic_title",
            "academic_degree",
            "academic_degree",
        ]
        for field in criteries:
            value = locals()[field]
            if value:
                sub_query.append(f"{field} = ?")
                params.append(value)

        if fio:
            sub_query.append(f"fio LIKE ?")
            params.append(f"%{fio}%")

        return sub_query, params

    def search_teachers(
        self, faculty, department, fio, academic_title, academic_degree, limit, offset
    ) -> tuple[int, list[Teacher]]:
        sub_query, params = self._build_search_dongition(
            faculty, department, fio, academic_title, academic_degree
        )

        where_sub_query = " WHERE " + " AND ".join(sub_query) if sub_query else ""

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            total_query = f"SELECT COUNT(*) FROM teachers{where_sub_query}"
            cursor.execute(total_query, params)
            total = cursor.fetchone()[0]

            where_sub_query += " LIMIT ? OFFSET ?"
            params.append(limit)
            params.append(offset)

            query = f"SELECT * FROM teachers {where_sub_query}"
            cursor = conn.execute(query, params)

            teachers = [Teacher.get_teacher_from_row(row) for row in cursor.fetchall()]
            return total, teachers

    def delete_teachers(
        self, faculty, department, fio, academic_title, academic_degree
    ) -> int:
        sub_query, params = self._build_search_dongition(
            faculty, department, fio, academic_title, academic_degree
        )

        where_sub_query = " WHERE " + " AND ".join(sub_query) if sub_query else ""

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            query = f"DELETE FROM teachers{where_sub_query}"
            cursor = conn.execute(query, params)
            count = cursor.rowcount
            conn.commit()
            return count
