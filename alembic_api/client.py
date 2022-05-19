from typing import List
from typing import Optional

from alembic_api.cfg import AlembicConfig


class AlembicClient(AlembicConfig):
    def __init__(
        self,
        cfg_name: Optional[str] = None,
        cfg_path: Optional[str] = None
    ):
        super().__init__(cfg_name=cfg_name, cfg_path=cfg_path)

    def head(self) -> str:
        return self._script.get_current_head()

    def heads(self) -> List[str]:
        return self._script.get_heads()
