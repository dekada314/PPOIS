from src.model.teacher import Teacher


def test_get_teacher_from_row_maps_fields_correctly():
    row = [1, "ФКСИС", "ИИТ", "Иванов Иван", "доцент", "кандидат наук", 12.5]

    teacher = Teacher.get_teacher_from_row(row)

    assert teacher == Teacher(
        faculty="ФКСИС",
        department="ИИТ",
        fio="Иванов Иван",
        academic_title="доцент",
        academic_degree="кандидат наук",
        work_experience=12.5,
    )


def test_get_teacher_from_row_returns_none_for_empty_row():
    assert Teacher.get_teacher_from_row([]) is None
