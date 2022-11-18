from dataclasses import dataclass

from app.api import schema
from app.exceptions import exceptions as exception


@dataclass
class ValidationService:
    """Сервис валидации входных параметров."""

    async def validate(
            self, user_id: str, item_id: list[str]
    ) -> list[schema.CheckAPIResponse]:
        """Валидировать входные параметры."""

        return []
