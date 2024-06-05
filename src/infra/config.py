import os
from pydantic_settings import BaseSettings, SettingsConfigDict
abs_path_env = os.path.abspath('../../../.env')


class Settings(BaseSettings):
    PROJECT_NAME: str = "TDD API"
    ROOT_PATH: str = "/"
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=abs_path_env, env_file_encoding='utf-8')


settings = Settings()
