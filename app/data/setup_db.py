import sqlite3


conn = sqlite3.connect(
    "app/data/demo.db"
)

cursor = conn.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS courses(

id INTEGER,

name TEXT

)

""")


cursor.execute("""

INSERT INTO courses
VALUES
(1,'DBMS'),
(2,'AI')

""")


conn.commit()

conn.close()


print(
"DB Ready"
)