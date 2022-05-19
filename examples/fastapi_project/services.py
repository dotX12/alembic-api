from alembic_api import AlembicClient, AlembicServer


class AlembicService:
    def __init__(self, client: AlembicClient, server: AlembicServer):
        self.client = client
        self.server = server

    def get_client_revision(self):
        return self.client.head()

    def get_client_heads(self):
        return self.client.heads()

    def get_server_revision(self):
        return self.server.revision()

    def check_server_is_client_revision(self):
        return self.get_client_revision() == self.get_server_revision()
