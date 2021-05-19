from sqlalchemy import Column, Integer, String

from database.database import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
