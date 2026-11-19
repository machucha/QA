import pytest
from sqlalchemy import text, create_engine

from config import DB_CONNECTION_STRING

db = create_engine(DB_CONNECTION_STRING)


@pytest.fixture()
def student_id():
    new_id = 25
    with db.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO student (user_id, education_form) "
                "VALUES (:id, :form)"
            ),
            {"id": new_id, "form": "personal"},
        )
    yield new_id
    with db.begin() as conn:
        conn.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": new_id},
        )


@pytest.fixture()
def subject_id():
    new_id = 16
    with db.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (:id, :title)"
            ),
            {"id": new_id, "title": "algebra"},
        )
    yield new_id
    with db.begin() as conn:
        conn.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": new_id},
        )