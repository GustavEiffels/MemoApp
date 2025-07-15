from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MYSQL_USER: str = "myuser"
    MYSQL_PASSWORD: str = "mypassword"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = "33066"
    MYSQL_DATABASE: str = "mydb"

    APP_NAME: str = "memoApp"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+pymysql://"
            f"{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore'
    )

settings = Settings()