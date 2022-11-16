from fastapi import FastAPI
from starlette.responses import Response


def add_healh_check(app: FastAPI):
    @app.get("/health", tags=["health"], summary="Health check")
    def health():
        return Response(content="OK")
