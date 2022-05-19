from contextlib import contextmanager

from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine


@contextmanager
def get_connection(engine: Engine) -> Connection:
    conn = engine.connect()
    yield conn
    conn.close()

