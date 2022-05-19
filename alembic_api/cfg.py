import os
from typing import Optional

from alembic.config import Config
from alembic.script import ScriptDirectory


class AlembicConfig:
    def __init__(
        self,
        cfg_path: str,
        cfg_name: Optional[str] = None,
    ):
        self.cfg_name = cfg_name
        self.cfg_path = cfg_path

    @property
    def _path(self) -> str:

        if self.cfg_path and self.cfg_name:
            return os.path.join(self.cfg_path, self.cfg_name)
        elif self.cfg_path and not self.cfg_name:
            return os.path.join(self.cfg_path, "alembic.ini")
        else:
            raise Exception(
                "You must specify the path to the folder "
                "where the configuration file is located."
            )

    @property
    def _config(self) -> Config:
        return Config(self._path)

    @property
    def _script(self) -> ScriptDirectory:
        return ScriptDirectory.from_config(self._config)
