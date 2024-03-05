from fill_db import fill
from create_test_db import create_db


def test(db_name: str, n: int) -> None:
    create_db(db_name)
    fill(db_name, n)


test("test.db", 10)