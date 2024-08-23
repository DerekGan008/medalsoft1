from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.api.endpoints import user, class_, assignment, submission

# 创建 FastAPI 实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Derek System!"}

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 包含 API 路由
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(class_.router, prefix="/classes", tags=["classes"])
app.include_router(assignment.router, prefix="/assignments", tags=["assignments"])
app.include_router(submission.router, prefix="/submissions", tags=["submissions"])
