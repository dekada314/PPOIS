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
            faculty=row[1],
            department=row[2],
            first_name=row[3],
            last_name=row[4],
            middle_name=row[5],
            academic_title=row[6],
            academic_degree=row[7],
            work_experience=row[8],
        )
