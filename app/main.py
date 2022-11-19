from fastapi import FastAPI
from app.api.endpoints.check import router as check_router
import uvicorn
from app.db.db import DataBaseConnector


def add_events(fastapi_app: FastAPI) -> None:
    db = DataBaseConnector()

    @fastapi_app.on_event("startup")
    async def startup_event() -> None:
        await db.connect()

    @fastapi_app.on_event("shutdown")
    async def shutdown_event() -> None:
        await db.disconnect()


def create_app() -> FastAPI:
    """Создает FastAPI app."""

    fast_api_app = FastAPI()
    fast_api_app.include_router(check_router)

    # add_events(fast_api_app)

    return fast_api_app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
