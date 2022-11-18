from dataclasses import dataclass
from typing import Any, Optional

import asyncpg

from app.config import settings


class Singleton(type):
    _instances: dict = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any) -> object:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class DataBaseConnector(metaclass=Singleton):
    """Класс для подключения к базе данных."""

    _db: Optional[asyncpg.Pool] = None

    @property
    def db(self) -> asyncpg.Pool:
        """Возвращает подключение к базе данных."""
        assert self._db is not None, "Не подключено к базе данных"
        return self._db

    async def connect(self) -> None:
        """Подключиться к базе данных."""
        self._db = await asyncpg.create_pool(**settings.db_creds)

    async def disconnect(self) -> None:
        """Отключиться от базы данных."""
        if self._db:
            await self._db.close()
