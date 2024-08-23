import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Settings:
    # 数据库配置
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://DEREK:Derekgan@localhost/derek_db")
    
    # Redis 配置（可选）
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # 其他配置项
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# 实例化 Settings 类
settings = Settings()
