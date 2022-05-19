import os
from typing import Optional

from alembic.config import Config
from alembic.script import ScriptDirectory

from alembic_api.utils import get_current_path


class AlembicConfig:
    def __init__(
        self,
        cfg_name: Optional[str] = None,
        cfg_path: Optional[str] = None
    ):
        self.cfg_name = cfg_name
        self.cfg_path = cfg_path

    @property
    def _path(self) -> str:
        current_path = get_current_path()

        if self.cfg_path and self.cfg_name:
            return os.path.join(self.cfg_path, self.cfg_name)
        elif not self.cfg_path and self.cfg_name:
            return os.path.join(current_path, self.cfg_name)
        elif self.cfg_path and not self.cfg_name:
            return os.path.join(self.cfg_path, "alembic.ini")
        else:
            return os.path.join(current_path, "alembic.ini")

    @property
    def _config(self) -> Config:
        return Config(self._path)

    @property
    def _script(self) -> ScriptDirectory:
        return ScriptDirectory.from_config(self._config)
