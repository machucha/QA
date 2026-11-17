from sqlalchemy import text
from sqlalchemy import create_engine

db_connection_string = "postgresql://postgres:Immortals00@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert_student():
    sql = text(
        "INSERT INTO student (user_id, education_form) "
        "VALUES (:user_id, :education_form)"
    )
    db.execute(sql, user_id=25, education_form='personal')


def test_delete():
    sql = text("DELETE FROM student WHERE user_id = :id")
    db.execute(sql, id=25)
    check_sql = text("SELECT * FROM student WHERE user_id = :id")
    result = db.execute(check_sql, id=25).fetchone()
    assert result is None
