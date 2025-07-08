from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_uri: str = 'mysql+pymysql://myuser:mypassword@localhost:33066/mydb'
    app_name: str = 'Memo'

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()