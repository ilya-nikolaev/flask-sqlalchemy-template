from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models import User


def find_user(db: Session, username: str) -> User | None:
    query = select(User).where(User.username == username)
    user: User = db.scalar(query)

    return user
