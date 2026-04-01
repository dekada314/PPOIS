from dataclasses import dataclass, field


@dataclass(slots=True)
class Teacher:
    faculty: str = ""
    department: str = ""
    fio: str = ""
    academic_title: str = ""
    academic_degree: str = ""
    work_experience: float = 0

    @classmethod
    def get_teacher_from_row(cls, row: list) -> "Teacher":
        if not row:
            return None

        return cls(
            faculty=row[1],
            department=row[2],
            fio=row[3],
            academic_title=row[4],
            academic_degree=row[5],
            work_experience=row[6],
        )
