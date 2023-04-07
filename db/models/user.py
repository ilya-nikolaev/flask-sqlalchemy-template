from db.models.base import Base
from sqlalchemy import Column
from sqlalchemy import BigInteger, Text


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)

    username = Column(Text, nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
