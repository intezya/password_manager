import random
import sqlite3
import string


def fill(db_name: str, n: int) -> None:
    db_name = rf'db/{db_name}'
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    for _ in range(n):
        title = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        link = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        notes = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

        cur.execute(
            """INSERT INTO passwords
             VALUES (?, ?, ?, ?, ?)""", (title, username, password, link, notes))

    con.commit()