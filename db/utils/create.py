from sqlalchemy import create_engine, Engine

from config import load_config
from db.models.base import Base


def get_engine():
    config = load_config()

    return create_engine(
        f"postgresql+psycopg2://"
        f"{config.db.user}:"
        f"{config.db.pswd}@"
        f"{config.db.host}:"
        f"{config.db.port}/"
        f"{config.db.name}"
    )


def create_db(db_engine: Engine):
    Base.metadata.create_all(bind=db_engine)
