import os

from fastapi import FastAPI

from alembic_api import AlembicClient
from alembic_api import AlembicServer
from binding import own_router
from examples.fastapi_project.dependencies import HealthCheckDependencyMarker
from examples.fastapi_project.services import AlembicService


def get_application_v2() -> FastAPI:
    application = FastAPI(
        debug=False,
        docs_url=None,
        title='Test Project',
    )
    application.include_router(own_router)

    application.dependency_overrides.update(
        {
            HealthCheckDependencyMarker: lambda: AlembicService(
                client=AlembicClient(
                    cfg_name="alembic.ini",
                    cfg_path=os.path.dirname(__file__),
                ),
                server=AlembicServer(
                    engine="sync_engine",
                )
            )
        }
    )
    #     sync_engine - create_engine(DSN)

    return application
