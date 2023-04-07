from flask import Flask
from flask import session, g

from db.models import User


class UserMiddleware:
    def __init__(self, app: Flask):
        app.before_request(self.open)

    @staticmethod
    def open():
        user_id = session.get("user_id")
        if user_id:
            user = g.db.get(User, int(user_id))
            g.current_user = user
        else:
            g.current_user = None
