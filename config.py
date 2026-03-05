from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///auth.db"
    SECRET_KEY: str = "SUPER_SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 2

settings = Settings()