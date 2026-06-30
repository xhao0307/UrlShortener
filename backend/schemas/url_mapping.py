from pydantic import BaseModel, HttpUrl

# 创建短链请求体
class UrlCreateRequest(BaseModel):
    original_url: HttpUrl

# 创建短链返回体
class UrlCreateResponse(BaseModel):
    short_url: str
    short_code: str
    original_url: str