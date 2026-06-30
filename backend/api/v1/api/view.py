from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.url_mapping import UrlCreateRequest, UrlCreateResponse
from crud.url_mapping import create_url_mapping, get_url_by_code, increase_click
from core.config import settings

router = APIRouter(prefix="/api", tags=["短链接服务"])

# 接口1：POST /api/shorten 创建短链接（需求指定）
@router.post("/shorten", response_model=UrlCreateResponse)
def create_short_url(req: UrlCreateRequest, db: Session = Depends(get_db)):
    db_record = create_url_mapping(db, str(req.original_url))
    short_url = f"{settings.BASE_URL}/{db_record.short_code}"
    return UrlCreateResponse(
        short_url=short_url,
        short_code=db_record.short_code,
        original_url=db_record.original_url
    )

