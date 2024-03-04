import sqlite3
from hashlib import sha256


def create_table(con, password):
    password = sha256(password.encode()).hexdigest()

    cur = con.cursor()

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
         VALUES (?)""", (password,))

    con.commit()


def create_con(db_path, password) -> sqlite3.connect:
    password = sha256(password.encode()).hexdigest()

    con = sqlite3.connect(db_path)

    cur = con.cursor()

    cur.execute(
      """SELECT password
         FROM master_key
         WHERE password = ?""", (password,))

    if not cur.fetchone():
        return False

    return con
