from sqlalchemy import Column, String, Integer, DateTime, func
from db.session import Base

class UrlMap(Base):
    __tablename__ = "url_mapping"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    original_url = Column(String(2048), nullable=False)
    click_count = Column(Integer, default=0, comment="访问点击统计")
    create_time = Column(DateTime(timezone=True), server_default=func.now())