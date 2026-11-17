from sqlalchemy import text
from sqlalchemy import create_engine

db_connection_string = "postgresql://postgres:Immortals00@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert_subject():
    sql = text(
        "INSERT INTO subject (subject_id, subject_title) "
        "VALUES (:id, :title)"
    )
    db.execute(sql, id=16, title='algebra')


def test_update():
    sql = text(
        "UPDATE subject SET subject_title = :title "
        "WHERE subject_id = :id"
    )
    db.execute(sql, title='Algebra', id=16)
    check_sql = text("SELECT subject_title FROM subject WHERE subject_id = :id")
    result = db.execute(check_sql, id=16).fetchone()
    assert result[0] == 'Algebra'


def test_delete():
    sql = text(
        "DELETE FROM subject "
        "WHERE subject_id = :id AND subject_title = :title"
    )
    db.execute(sql, id=16, title='Algebra')
