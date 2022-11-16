# app/config.py
import os

from sqlalchemy.engine.url import URL
from starlette.config import Config as StarletteConfig, environ
from starlette.datastructures import Secret

get_config: StarletteConfig = StarletteConfig()

PROJECT_NAME = "Motimatic Exercise - Student Service"
SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

ENVIRONMENT = environ.get("ENVIRONMENT", "development")
DB_HOST = get_config("POSTGRES_HOST", cast=str, default="localhost")
DB_PORT = get_config("POSTGRES_PORT", cast=int, default=5433)
DB_NAME = get_config("POSTGRES_DB", cast=str, default="studentsdb")
DB_USER = get_config("POSTGRES_USER", cast=str, default="postgres")
DB_PASS = get_config("POSTGRES_PASSWORD", cast=Secret, default="p@ssw0rD")
DB_SSL = get_config("POSTGRES_SSL", cast=str, default="prefer")
TESTING = get_config("TESTING", cast=bool, default=False)
POSTGRES_CONN_TIMEOUT = get_config("POSTGRES_CONN_TIMEOUT", cast=int, default=None)
POSTGRES_CONN_MAX_IDLE = get_config("POSTGRES_CONN_MAX_IDLE", cast=int, default=None)
POSTGRES_CONN_MAX_OPEN = get_config("POSTGRES_CONN_MAX_OPEN", cast=int, default=None)
POSTGRES_CONN_MAX_LIFE = get_config("POSTGRES_CONN_MAX_LIFE", cast=int, default=None)


SQLECHO = get_config("SQLECHO", cast=bool, default=None)

DATABASE_URL: URL = URL.create(
    "postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    query={"sslmode": DB_SSL},
)


def set_environment(env: str):
    environ["ENVIRONMENT"] = env
