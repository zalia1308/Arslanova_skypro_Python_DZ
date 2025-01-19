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
        # Начинаем транзакцию
        db.execute(text("BEGIN"))
        try:
              # Добавляем запись
              sql = text("insert into subject(\"subject_title\") values (:new_subject_title)")
              rows = db.execute(sql, {'new_subject_title':'Zalia'})
              # Проверяем, что запись добавлена
              sql_check = text("SELECT * FROM subject WHERE subject_title = :title")
              row = db.execute(sql_check, {'title': 'Zalia'}).fetchone()
              assert row, "Subject 'Zalia' was added"
        finally:
              # Откатываем транзакцию
              db.execute(text("ROLLBACK"))


def test_update_subject():
    with engine.connect() as db:
        # Начинаем транзакцию
        db.execute(text("BEGIN"))
        try:
              # Добавляем запись
              sql_create = text("insert into subject(\"subject_title\") values (:new_subject_title)")
              rows_create = db.execute(sql_create, {'new_subject_title':'Zalia'})
              # Изменяем запись
              sql_update = text("update subject set subject_id = :id where subject_title = :title")
              rows_update = db.execute(sql_update, {'id': 25, 'title': 'Zalia'})
              # Проверяем, что запись изменена
              sql_check = text("SELECT * FROM subject WHERE subject_id = :id")
              row = db.execute(sql_check, {'id': '25'}).fetchone()
              assert row, "Subject '25' was added"
        finally:
              # Откатываем транзакцию
              db.execute(text("ROLLBACK"))


def test_delete_subject():
    with engine.connect() as db:
        sql_create = text("insert into subject(\"subject_title\") values (:new_subject_title)")
        rows_create = db.execute(sql_create, {'new_subject_title': 'Zalia'})
        sql_delete = text("delete from subject where subject_title = :new_subject_title")
        rows_delete = db.execute(sql_delete, {'new_subject_title': 'Zalia'})