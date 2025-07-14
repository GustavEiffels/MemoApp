import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    USER = os.getenv("MYSQL_USER")
    PASSWORD = os.getenv("PASSWORD")
    DB_URL = os.getenv("DB_URL")
    DB_NAME = os.getenv("DB_NAME")
    database_uri: str = f'mysql+pymysql://{USER}:{PASSWORD}@{DB_URL}/{DB_NAME}'
    app_name: str = 'Memo'

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()