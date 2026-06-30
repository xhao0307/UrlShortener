FROM python:3.13-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install uv && \
    rm -rf /root/.cache/pip

# 分层缓存依赖
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache && rm -rf /root/.cache/uv

COPY . .

EXPOSE 8000
# 容器强制0.0.0.0，关闭reload，不受settings控制
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]