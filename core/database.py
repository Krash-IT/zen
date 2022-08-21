from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, Integer

from core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    __name__: str
    id: Any

    created_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    updated_timestamp = Column(DateTime(timezone=True), onupdate=func.now())

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
