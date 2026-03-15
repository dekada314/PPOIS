from dataclasses import dataclass, field


@dataclass(slots=True)
class Teacher:
    faculty: str
    department_name: str 
    fio: str
    academic_title: str
    academic_degree: str
    work_expirience: float
    
    
d = Teacher('asdfads,','asdf')
print(d)