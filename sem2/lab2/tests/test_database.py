import sqlite3

import pytest

from src.model.database import Database
from src.model.teacher import Teacher


@pytest.fixture
def sample_teachers() -> list[Teacher]:
    return [
        Teacher(
            faculty="ФКСИС",
            department="ИИТ",
            fio="Иванов Иван",
            academic_title="доцент",
            academic_degree="кандидат наук",
            work_experience=11.0,
        ),
        Teacher(
            faculty="ФКСИС",
            department="ПОИТ",
            fio="Петров Петр",
            academic_title="профессор",
            academic_degree="доктор наук",
            work_experience=21.0,
        ),
        Teacher(
            faculty="ФРЭ",
            department="ИИТ",
            fio="Сидоров Сидор",
            academic_title="ассистент",
            academic_degree="магистр",
            work_experience=3.0,
        ),
    ]


@pytest.fixture
def db(tmp_path, sample_teachers) -> Database:
    db_path = tmp_path / "teachers.sqlite3"
    database = Database(str(db_path))
    for teacher in sample_teachers:
        database.add_teacher(teacher)
    return database


def test_database_creates_teachers_table(tmp_path):
    db_path = tmp_path / "teachers.sqlite3"
    Database(str(db_path))

    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='teachers'"
        )
        assert cursor.fetchone()[0] == "teachers"


def test_add_and_count_records(db):
    assert db.get_records_count() == 3


def test_get_all_departments_returns_distinct_values(db):
    assert set(db.get_all_deprtments()) == {"ИИТ", "ПОИТ"}


def test_get_all_academic_titles_returns_distinct_values(db):
    assert set(db.get_all_academic_titles()) == {"доцент", "профессор", "ассистент"}


def test_get_teachers_page_returns_limited_subset(db):
    page = db.get_teachers_page(limit=2, offset=1)

    assert len(page) == 2
    assert all(isinstance(item, Teacher) for item in page)


def test_get_all_teachers_returns_model_instances(db):
    teachers = db.get_all_teachers()

    assert len(teachers) == 3
    assert all(isinstance(item, Teacher) for item in teachers)


def test_build_search_condition_handles_empty_filters(db):
    sub_query, params = db._build_search_dongition("", "", "", "", "")

    assert sub_query == []
    assert params == []


def test_build_search_condition_adds_filters_and_like(db):
    sub_query, params = db._build_search_dongition(
        "ФКСИС", "ИИТ", "Иван", "доцент", "кандидат наук"
    )

    assert "faculty = ?" in sub_query
    assert "department = ?" in sub_query
    assert "academic_title = ?" in sub_query
    assert "academic_degree = ?" in sub_query
    assert "fio LIKE ?" in sub_query
    assert "%Иван%" in params


def test_search_teachers_with_pagination_and_total(db):
    total, teachers = db.search_teachers("", "", "", "", "", limit=2, offset=0)

    assert total == 3
    assert len(teachers) == 2


