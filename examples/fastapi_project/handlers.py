from fastapi import APIRouter
from fastapi import Depends
from starlette.responses import Response

from dependencies import HealthCheckDependencyMarker
from services import AlembicService

healthcheck_router = APIRouter()


@healthcheck_router.get(
    "/healthcheck",
)
async def healthcheck_handler(
    service: AlembicService = Depends(HealthCheckDependencyMarker),
):

    client_headers = service.get_client_heads()

    if len(client_headers) > 1:
        return Response(status_code=503)
    if not service.check_server_is_client_revision():
        return Response(status_code=503)
    return Response(200)

