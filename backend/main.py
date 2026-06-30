from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db.session import engine, Base, get_db
from models.url_mapping import UrlMap  # 导入模型自动建表
from api.v1.api.view import router as url_router
from crud.url_mapping import get_url_by_code, increase_click
from core.config import settings

# 启动自动创建数据表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener 短链接服务", version="1.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册API接口 /api/shorten
app.include_router(url_router)

# 需求核心路由：GET /{short_code} 302重定向
@app.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    record = get_url_by_code(db, short_code)
    if not record:
        raise HTTPException(status_code=404, detail="短链接不存在")
    # 访问统计：点击数+1
    increase_click(db, record)
    # 302临时重定向
    return RedirectResponse(record.original_url, status_code=302)

# 根页面测试
@app.get("/")
def index():
    return {"msg": "短链接服务运行中，访问 /docs 查看接口文档"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.ENV == "dev"
    )