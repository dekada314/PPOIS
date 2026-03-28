from dataclasses import dataclass, field


@dataclass(slots=True)
class Teacher:
    id: int = 0
    faculty: str = ""
    department: str = ""
    first_name: str = ""
    last_name: str = ""
    middle_name: str = ""
    academic_title: str = ""
    academic_degree: str = ""
    work_experience: float = 0

    @classmethod
    def get_teacher_from_row(cls, row: list) -> "Teacher":
        if not row:
            return None

        return cls(
            faculty=row[0],
            department=row[1],
            fio=row[2],
            academic_title=row[3],
            academic_degree=row[4],
            work_experience=row[5],
        )
