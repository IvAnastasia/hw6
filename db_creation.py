import sqlite3
db = sqlite3.connect('inglhart.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY,
    born_year INT,
    gender TEXT,
    education TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Responses (
    id INT PRIMARY KEY,
    stress INT,
    happiness INT,
    proudness INT,
    labor INT,
    two_leaders INT,
    rules INT
)
""")
db.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS Questions (
    question_id INT PRIMARY KEY,
    question TEXT
)
""")
db.commit()

cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (1, "Как часто вы себя чувствуете нервным или напряжённым?")
""")
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (2, "Вы счастливый человек?")
""")
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (3, "Вы гордитесь быть гражданином своей страны?")
""")
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (4, "Упорный труд - самый надёжный путь к достижению результатов")
""")
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (5, "Необходимо любой ценой избегать создания таких структур, в которых подчинённые будут иметь двух начальников")
""")
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (6, "Правила организации не должны нарушаться, даже если работнику кажется, что это в интересах компании")
""")

db.commit()