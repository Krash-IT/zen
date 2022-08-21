from email.policy import default
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

from core.database import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), default=uuid4)
    email = Column(String(30))
    password = Column(String, index=True)

    first_name = Column(String(50))
    middle_name = Column(String(30), nullable=True)
    last_name = Column(String(50))
    image_url = Column(String(255), index=True)
    gender = Column(String(30))

    title = Column(String(30), nullable=True)
    level = Column(String(30))
    status = Column(String(30))
    phone = Column(String(30), nullable=True)
    nationality = Column(String(30))

    next_of_kin_first_name = Column(String(30), nullable=True)
    next_of_kin_last_name = Column(String(30), nullable=True)
    next_of_kin_phone = Column(String(15), nullable=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"
