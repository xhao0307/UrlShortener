from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import SQLALCHEMY_DATABASE_URL
import os

# 自动创建db文件夹
db_dir = os.path.dirname(SQLALCHEMY_DATABASE_URL.replace("sqlite:///", ""))
os.makedirs(db_dir, exist_ok=True)

# SQLite引擎必须加 check_same_thread=False
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 数据库会话依赖注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()