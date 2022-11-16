import logging
from starlette.requests import Request

from app.models.meta import Session


async def db_middleware_handler(request: Request, call_next):
    try:
        request.state.db = Session()
        response = await call_next(request)
        request.state.db.close()
        return response
    except Exception as exc:
        logging.error(exc, exc_info=True)
        if request.state.db:
            request.state.db.rollback()
    finally:
        if request.state.db:
            request.state.db.close()


def get_db(request: Request):
    return request.state.db
