from ..config import (
    DATABASE_URL,
    POSTGRES_CONN_MAX_IDLE,
    POSTGRES_CONN_MAX_OPEN,
    POSTGRES_CONN_TIMEOUT,
    SQLECHO,
)

from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# https://github.com/psycopg/psycopg2/issues/550
import psycopg2.extensions  # noqa

connect_args = {"connect_timeout": POSTGRES_CONN_TIMEOUT}


engine_args = dict(
    connect_args=connect_args,
    pool_pre_ping=True,
    echo=SQLECHO,
    echo_pool=SQLECHO,
    pool_recycle=POSTGRES_CONN_MAX_IDLE,
    max_overflow=POSTGRES_CONN_MAX_OPEN,
    pool_size=POSTGRES_CONN_MAX_IDLE,
    pool_timeout=POSTGRES_CONN_TIMEOUT,
)
defined_engine_args = {k: v for k, v in engine_args.items() if v is not None}

engine = create_engine(DATABASE_URL, **defined_engine_args)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine_util = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=1,
    echo=SQLECHO,
    echo_pool=SQLECHO,
    connect_args=connect_args,
)
db_util_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine_util))


Base = declarative_base()


def migrate():
    with engine.begin() as connection:
        alembic_cfg = Config("./alembic.ini")
        alembic_cfg.attributes["connection"] = connection
        command.upgrade(alembic_cfg, "head")
