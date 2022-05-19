from typing import Tuple

from alembic.runtime.migration import MigrationContext
from sqlalchemy.engine import Engine
from sqlalchemy.future import Connection

from alembic_api.decorators import get_connection


def get_context(connection: Connection) -> MigrationContext:
    return MigrationContext.configure(connection=connection)


class AlembicServer:
    def __init__(self, engine: Engine):
        self.engine = engine

    def revision(self) -> str:
        with get_connection(engine=self.engine) as conn:
            context = MigrationContext.configure(conn)
            return context.get_current_revision()

    def heads(self) -> Tuple[str]:
        with get_connection(engine=self.engine) as conn:
            context = MigrationContext.configure(conn)
            return context.get_current_heads()
