from typing import List, Union, Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./test.db"   # temporary fallback
    OPENAI_API_KEY: str = "dummy_key"           # temporary fallback
    # Accept string or list to avoid dotenv JSON parsing; normalize via validator
    ALLOWED_ORIGINS: Optional[Union[str, List[str]]] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(
        cls, value: Optional[Union[str, List[str]]]
    ) -> List[str]:
        if value is None:
            return ["*"]
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return ["*"]
            return [origin.strip() for origin in stripped.split(",") if origin.strip()]
        return ["*"]

settings = Settings()

