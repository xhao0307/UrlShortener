# UrlShortener

一个前后端分离的短链接生成服务。用户在页面输入原始 URL 后，系统会生成一个短链接；访问短链接时，后端会根据短码查找原始地址并返回 302 重定向，同时记录点击次数。

## 功能特性

- 生成短链接：通过 `POST /api/shorten` 创建原始 URL 与短码的映射。
- 短链跳转：访问 `/{short_code}` 自动重定向到原始 URL。
- 点击统计：每次访问短链时自动累加 `click_count`。
- 自动建表：后端启动时通过 SQLAlchemy 自动创建 SQLite 数据表。
- 前端页面：基于 Next.js 提供短链接生成界面。
- 容器化部署：通过 Docker Compose 同时启动前端和后端服务。

## 技术栈

### 后端

- Python 3.13
- FastAPI
- SQLAlchemy 2.x
- Pydantic 2.x
- SQLite
- uv

### 前端

- Next.js 16
- React 19
- TypeScript
- Tailwind CSS 4
- Axios

## 项目结构

```text
.
├── backend/                 # FastAPI 后端服务
│   ├── api/v1/api/           # API 路由
│   ├── core/                 # 配置与短码生成逻辑
│   ├── crud/                 # 数据访问逻辑
│   ├── db/                   # 数据库连接与 SQLite 数据目录
│   ├── models/               # SQLAlchemy 模型
│   ├── schemas/              # Pydantic 请求/响应模型
│   ├── main.py               # 后端入口
│   ├── pyproject.toml        # Python 依赖配置
│   └── Dockerfile
├── frontend/                 # Next.js 前端应用
│   ├── app/                  # App Router 页面
│   ├── api/                  # 前端接口封装
│   ├── components/           # 页面组件
│   ├── utils/                # 工具函数
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml        # 前后端容器编排
├── test.js
└── test.ts
```

## 环境变量

后端依赖 `backend/.env`，需要包含以下配置：

```env
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
ENV=dev
SQLITE_DB_PATH=./db/sqlite/short.db
BASE_URL=http://127.0.0.1:8000
SHORT_CODE_LENGTH=6
```

字段说明：

- `SERVER_HOST`：本地开发时后端监听地址。
- `SERVER_PORT`：后端监听端口。
- `ENV`：运行环境，值为 `dev` 时本地启动会开启 reload。
- `SQLITE_DB_PATH`：SQLite 数据库文件路径。
- `BASE_URL`：生成短链接时使用的基础地址。
- `SHORT_CODE_LENGTH`：短码长度。

## 使用 Docker Compose 启动

在项目根目录执行：

```bash
docker compose up --build
```

启动后访问：

- 前端页面：`http://127.0.0.1:3000`
- 后端接口文档：`http://127.0.0.1:8000/docs`
- 后端健康测试：`http://127.0.0.1:8000/`

Docker Compose 会将 `backend/db` 挂载到容器内 `/app/db`，SQLite 数据会保留在本地项目目录中。

## 本地开发启动

### 启动后端

```bash
cd backend
uv sync
uv run python main.py
```

后端默认运行在 `http://127.0.0.1:8000`。

### 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端默认运行在 `http://127.0.0.1:3000`。

前端通过 `frontend/next.config.ts` 配置了 API 代理：

- 本地开发：`/api/*` 转发到 `http://127.0.0.1:8000/api/*`
- Docker 生产运行：`/api/*` 转发到 `http://backend:8000/api/*`

## API 示例

### 创建短链接

```bash
curl -X POST http://127.0.0.1:8000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"original_url":"https://example.com"}'
```

响应示例：

```json
{
  "short_url": "http://127.0.0.1:8000/a1B2c3",
  "short_code": "a1B2c3",
  "original_url": "https://example.com/"
}
```

### 访问短链接

```bash
curl -I http://127.0.0.1:8000/a1B2c3
```

如果短码存在，服务会返回 `302` 并跳转到原始 URL；如果短码不存在，会返回 `404`。

## 数据模型

短链接数据存储在 `url_mapping` 表中，主要字段包括：

- `id`：主键。
- `short_code`：唯一短码。
- `original_url`：原始 URL。
- `click_count`：访问次数。
- `create_time`：创建时间。

## 常用命令

```bash
# 前端代码检查
cd frontend && npm run lint

# 前端生产构建
cd frontend && npm run build

# 后端本地启动
cd backend && uv run python main.py

# Docker Compose 启动
docker compose up --build
```
