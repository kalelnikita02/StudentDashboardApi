import os
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

cdb = None
DBSession: sessionmaker = None
Base = None


class Settings:
    PROJECT_NAME: str = "tagsmart"
    POSTGRES_USER: str = "timescaledb"
    POSTGRES_PASSWORD ="password"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = 5433 # default postgres port is 5432
    POSTGRES_DB: str = "student_data"
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()

engine = create_engine(settings.DATABASE_URL, connect_args={'connect_timeout': 2}, pool_size=0, max_overflow=-1,
                       pool_recycle=3600)

try:
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    logger.info("Database connected successfully")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as err:
    logger.error("Database Connection Error - {}".format(err))