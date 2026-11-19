from sqlalchemy import text

from conftest import db


def test_insert_subject():
    new_id = 17
    try:
        with db.begin() as conn:
            conn.execute(
                text(
                    "INSERT INTO subject (subject_id, subject_title) "
                    "VALUES (:id, :title)"
                ),
                {"id": new_id, "title": "algebra"},
            )

        with db.begin() as conn:
            row = conn.execute(
                text(
                    "SELECT subject_id, subject_title FROM subject "
                    "WHERE subject_id = :id"
                ),
                {"id": new_id},
            ).fetchone()

        assert row is not None
        assert row.subject_id == new_id
        assert row.subject_title == "algebra"
    finally:
        with db.begin() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": new_id},
            )


def test_update_subject(subject_id):
    with db.begin() as conn:
        conn.execute(
            text(
                "UPDATE subject SET subject_title = :title "
                "WHERE subject_id = :id"
            ),
            {"id": subject_id, "title": "Algebra"},
        )

    with db.begin() as conn:
        row = conn.execute(
            text(
                "SELECT subject_title FROM subject WHERE subject_id = :id"
            ),
            {"id": subject_id},
        ).fetchone()

    assert row is not None
    assert row.subject_title == "Algebra"


def test_delete_subject(subject_id):
    with db.begin() as conn:
        conn.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": subject_id},
        )

    with db.begin() as conn:
        row = conn.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": subject_id},
        ).fetchone()

    assert row is None