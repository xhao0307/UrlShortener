from sqlalchemy.orm import Session
from models.url_mapping import UrlMap
from core.base62 import generate_short_code
from core.config import settings

def create_url_mapping(db: Session, original_url: str) -> UrlMap:
    """创建短链映射，循环生成不重复短码"""
    while True:
        code = generate_short_code(settings.SHORT_CODE_LENGTH)
        exist = db.query(UrlMap).filter(UrlMap.short_code == code).first()
        if not exist:
            break
    db_map = UrlMap(short_code=code, original_url=original_url)
    db.add(db_map)
    db.commit()
    db.refresh(db_map)
    return db_map

def get_url_by_code(db: Session, short_code: str) -> UrlMap | None:
    """根据短码查询记录"""
    return db.query(UrlMap).filter(UrlMap.short_code == short_code).first()

def increase_click(db: Session, db_map: UrlMap):
    """访问时点击数+1（加分项访问统计）"""
    db_map.click_count += 1
    db.commit()