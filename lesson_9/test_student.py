from sqlalchemy import text

from conftest import db


def test_insert_student():
    new_id = 26
    try:
        with db.begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO student (user_id, education_form) "
                    "VALUES (:id, :form)"
                ),
                {"id": new_id, "form": "personal"},
            )

        with db.begin() as conn:
            row = conn.execute(
                text(
                    "SELECT user_id, education_form FROM student "
                    "WHERE user_id = :id"
                ),
                {"id": new_id},
            ).fetchone()

        assert row is not None
        assert row.user_id == new_id
        assert row.education_form == "personal"
    finally:
        with db.begin() as conn:
            conn.execute(
                text("DELETE FROM student WHERE user_id = :id"),
                {"id": new_id},
            )


def test_update_student(student_id):
    with db.begin() as conn:
        conn.execute(
            text(
                "UPDATE student SET education_form = :form "
                "WHERE user_id = :id"
            ),
            {"id": student_id, "form": "full_time"},
        )

    with db.begin() as conn:
        row = conn.execute(
            text(
                "SELECT education_form FROM student WHERE user_id = :id"
            ),
            {"id": student_id},
        ).fetchone()

    assert row is not None
    assert row.education_form == "full_time"


def test_delete_student(student_id):
    with db.begin() as conn:
        conn.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": student_id},
        )

    with db.begin() as conn:
        row = conn.execute(
            text("SELECT * FROM student WHERE user_id = :id"),
            {"id": student_id},
        ).fetchone()

    assert row is None