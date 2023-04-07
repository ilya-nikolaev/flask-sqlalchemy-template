import logging

from flask import Flask
from sqlalchemy.orm import sessionmaker

from app.views import register_auth_views
from config import load_config
from app.middlewares import DBMiddleware, UserMiddleware
from db.utils.create import get_engine


def register_views(app: Flask):
    register_auth_views(app)


def setup_middlewares(app: Flask, db_factory: sessionmaker):
    DBMiddleware(app, db_factory)
    UserMiddleware(app)


def create_app() -> Flask:
    config = load_config()

    db_engine = get_engine()
    db_factory = sessionmaker(bind=db_engine)

    app = Flask(__name__)
    app.secret_key = config.app.secret_key

    register_views(app)
    setup_middlewares(app, db_factory)

    return app


if __name__ == '__main__':
    logging.info("App is running locally")
    create_app().run("127.0.0.1", port=5000)
