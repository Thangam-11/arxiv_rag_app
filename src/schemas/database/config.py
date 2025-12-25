from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings


class PostgreSQLSettings(BaseSettings):
    """PostgreSQL configuration settings."""

    database_url: str = Field(
        description="PostgreSQL database URL"
    )

    echo_sql: bool = Field(default=False)
    pool_size: int = Field(default=20)
    max_overflow: int = Field(default=0)

    model_config = ConfigDict(
        env_prefix="POSTGRES_",
        env_file=".env",
        extra="ignore",
    )
