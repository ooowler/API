from pydantic import BaseSettings


class PostgresSettings(BaseSettings):
    """Класс с настройками базы данных."""

    user: str = "postgres"
    password: str = "root"
    db: str = "test_db"
    host: str = "localhost"
    port: int = 5432

    @property
    def db_creds(self) -> dict:
        return {
            "user": self.user,
            "password": self.password,
            "database": self.db,
            "host": self.host,
            "port": self.port,
        }

    class Config:
        env_prefix = "POSTGRES_"
        env_file = ".env"


settings = PostgresSettings()
