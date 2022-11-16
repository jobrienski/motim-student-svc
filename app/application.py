# app/application.py

import logging

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from .config import ENVIRONMENT
from .lib.logs import get_level_from_environment, setup_logging
from .lib.server.db import db_middleware_handler
from .lib.server.error_handling import add_error_handling
from .lib.server.health import add_healh_check
from starlette.requests import Request
from .controllers import student_controller
from .models.meta import migrate


def create_app(title: str, environment=None, **kwargs) -> FastAPI:
    """Creates FastApi app, adds middleware, and health endpoint.
    :param title:
    :param environment:
    :return:
    :raises: OperationalError
    """
    if not environment:
        environment = ENVIRONMENT

    try:
        setup_logging(
            get_level_from_environment(environment),
            json_formatting=environment != "testing",
        )

        migrate()
    except OperationalError as dberr:
        logging.error(f"Error with database connection: {dberr}", exc_info=True)
        raise dberr
    except IOError as ioerr:
        logging.error(f"Error loading weights: {ioerr}")
        raise ioerr

    app: FastAPI = FastAPI(title=title, **kwargs)

    add_healh_check(app)
    add_error_handling(app)

    app.include_router(student_controller.router, prefix="/student")

    @app.middleware("http")
    def db_session_middleware(request: Request, call_next):
        return db_middleware_handler(request, call_next)

    return app
