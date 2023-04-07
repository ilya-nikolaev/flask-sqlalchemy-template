import os

from config import Config, AppConfig, DBConfig


def load_config() -> Config:
    return Config(
        app=AppConfig(secret_key=os.getenv("FLASK_SECRET_KEY")),
        db=DBConfig(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            pswd=os.getenv("DB_PSWD"),
            name=os.getenv("DB_NAME")
        )
    )
