from fastapi import APIRouter, Query, status

from app.api import schema
from app.api.validation import ValidationService

router = APIRouter()


@router.get(
    "/check",
    response_model=list[schema.CheckAPIResponse],
    status_code=status.HTTP_200_OK,
)
async def check_cart(
        example: str = Query(description="description", example="description"),
        example_list: list[str] = Query(
            description="description",
            example=["description", "description"],
        ),
) -> list[schema.CheckAPIResponse]:
    """Проверить корзину."""
    ValidationService()
    check_results = await ...

    return check_results
