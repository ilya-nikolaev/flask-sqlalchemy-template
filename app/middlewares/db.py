from flask import Flask, g
from sqlalchemy.orm import sessionmaker


class DBMiddleware:
    def __init__(self, app: Flask, db_factory: sessionmaker):
        self.db_factory = db_factory

        app.before_request(self.open)
        app.teardown_appcontext(self.close)

    def open(self):
        g.db = self.db_factory()

    @staticmethod
    def close(*_args, **_kwargs):
        g.db.close()
