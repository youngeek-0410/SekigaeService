import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_USER: str = os.getenv("DB_USER", "")
DB_NAME: str = os.getenv("DB_USER", "")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
DB_HOST: str = os.getenv("DB_HOST", "")
DB_PORT: str = os.getenv("DB_PORT", "")
DB_NAME: str = os.getenv("DB_NAME", "")
DATABASE_URL: str = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(DATABASE_URL, encoding="utf-8", echo=True)

# 実際の DB セッション
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = SessionLocal.query_property()


# Dependency Injection用
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
