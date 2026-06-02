from core.database import Base, engine
from sqlalchemy import Integer, String, Column,Boolean


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, index=True, primary_key=True)
    name_admin = Column(String(100), index=True)
    email = Column(String(50), index=True, unique=True)
    user_name = Column(String(50), index=True, unique=True)
    password = Column(String(18), index=True)
    is_write = Column(Boolean(True))
    changer_access = Column(Boolean(True))

Base.metadata.create_all(bind=engine)