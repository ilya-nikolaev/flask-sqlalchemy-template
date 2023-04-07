from sqlalchemy.orm import Session

from app.utils.auth import check_password
from db.funcs.user import find_user


def check_user(db: Session, username: str, password: str) -> int | None:
    user = find_user(db, username)

    if user is None:
        return None

    if check_password(password, user.password_hash):
        return user.id

    return None
