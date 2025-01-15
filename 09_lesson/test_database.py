from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:123@localhost:5432/QA"


engine = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(engine)
    names = inspector.get_table_names()
    assert names[0] == 'users'


def test_select_subject():
    with engine.connect() as db:
        rows = db.execute(text("SELECT * FROM subject where subject_id=2")).fetchone()
        row1 = rows
        assert row1._mapping['subject_id'] == 2
        assert row1._mapping ['subject_title'] == "Mathematics"


def test_create_subject():
    with engine.connect() as db:
        sql = text("insert into subject(\"subject_title\") values (:new_subject_title)")
        rows = db.execute(sql, {'new_subject_title':'Zalia'})
        db.commit()


def test_update_subject():
    with engine.connect() as db:
        sql = text("update subject set subject_id = :id where subject_title = :title")
        rows = db.execute(sql, {'id': 25, 'title' : 'Zalia'})
        db.commit()


def test_delete_subject():
    with engine.connect() as db:
        sql = text("delete from subject where subject_id = :id")
        rows = db.execute(sql, {'id': 25})
        db.commit()