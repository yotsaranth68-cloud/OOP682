from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. กำหนดชื่อไฟล์ฐานข้อมูล (จะถูกสร้างในโฟลเดอร์โปรเจกต์)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# 2. สร้าง Engine (สำหรับ SQLite ต้องมี check_same_thread=False)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. ตัวสร้าง Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()