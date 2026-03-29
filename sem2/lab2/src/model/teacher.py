from dataclasses import dataclass, field


@dataclass(slots=True)
class Teacher:
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
            first_name=row[2],
            last_name=row[3],
            middle_name=row[4],
            academic_title=row[5],
            academic_degree=row[6],
            work_experience=row[7],
        )
