import sqlite3
from hashlib import sha256

from typing import List, Tuple

from PyQt6.QtWidgets import QTableWidgetItem


def create_table(con: sqlite3.Connection,
                 password: str) -> None:
    password = sha256(password.encode()).hexdigest()

    with con.cursor() as cur:
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


def create_con(db_path,
               password) -> sqlite3.connect:
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


def getAllInfo(self: object) \
        -> List[Tuple[str, str, str, str, str]]:
    cur = self.con.cursor()

    cur.execute("""SELECT * FROM passwords""")

    return cur.fetchall()


def AddEntry(self: object,
             data: dict[str, str]) -> None:
    try:
        # Comes from addButton_clicked
        print(self.con)

        cur = self.con.cursor()

        cur.execute(
            """INSERT INTO passwords
             VALUES (?, ?, ?, ?, ?)""",
            (data["title"],
             data["username"],
             data["password"],
             data["link"],
             data["notes"]))

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        col = 0
        for key, value in data.items():
            item = QTableWidgetItem(str(value))
            self.tableWidget.setItem(row_position, col, item)
            col += 1
    except Exception as e:
        print(e)


def clearDB(self: object) -> None:
    cur = self.con.cursor()

    cur.execute("""DELETE FROM passwords""")

    self.con.commit()


def writeDB(self: object,
            data: List[List[any]]) -> None:
    clearDB(self)

    cur = self.con.cursor()

    insert_query = """INSERT INTO passwords 
                      (title, username, password, link, notes)
                      VALUES (?, ?, ?, ?, ?)"""

    for data_item in data:
        cur.execute(insert_query,
                    data_item)

    self.con.commit()