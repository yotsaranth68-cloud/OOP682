from sqlalchemy import Column, Integer, String, Boolean
from .database import Base  # ต้องมีไฟล์ database.py ที่นิยาม Base ไว้


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)