import sqlite3
import random
import string
from hashlib import sha256


def create_db(db_name: str) -> None:
    db_name = rf'db/{db_name}'

    with open(db_name, 'w'):
        pass

    con = sqlite3.connect(db_name)
    cur = con.cursor()
    password = 'test-db'

    cur.execute(
        """CREATE TABLE IF NOT EXISTS master_key
         (password text)""")

    cur.execute(
        """CREATE TABLE IF NOT EXISTS passwords
         (title text,
          username text,
          password text,
          link text,
          notes text)""")

    cur.execute(
        """INSERT INTO master_key
         VALUES (?)""", (sha256(password.encode()).hexdigest(),))

    con.commit()
