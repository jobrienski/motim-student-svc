from typing import Optional, Tuple

from fastapi.exceptions import HTTPException
import jwt
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from .token import JWTUser


class BearerAuthenticatedUser:
    header_key = "Authorization"
    prefix = "bearer"
    algorithms = ("RS256",)

    def __init__(self, *, claims: Optional[Tuple[str]] = None):
        """Create BearerAuthenticatedUser class, which parses the Authorization header and returns
        the claims.
        :param claims:
        """
        self.claims = claims

    @classmethod
    def jwt_user_from_token(cls, token: str, claims: Optional[Tuple[str]]) -> JWTUser:
        """Return user from token (only uid)
        :param token:
        :param claims:
        :return:
        :raises: PyJWTError
        """
        payload = jwt.decode(token, verify=False, algorithms=cls.algorithms)
        uid = payload.pop("uid", None)
        if claims:
            for k in set(claims) - set(payload):
                del payload[k]
        else:
            payload = {}

        return JWTUser(uid=uid, claims=payload)

    @classmethod
    def error_403(cls, message: str):
        return HTTPException(status_code=HTTP_403_FORBIDDEN, detail=message, headers={"WWW-Authenticate": "bearer"})

    @classmethod
    def parse_authorization_token(cls, request: Request) -> str:
        authorization: Optional[str] = request.headers.get(cls.header_key, None)
        if not authorization:
            raise cls.error_403("Forbidden")
        try:
            scheme, token = authorization.split()
            if scheme.lower() != cls.prefix.lower():
                raise cls.error_403(f"Authorization scheme {scheme} is not supported")
        except ValueError:
            raise cls.error_403("Could not separate Authorization scheme and token")

        return token

    async def __call__(self, request: Request) -> JWTUser:
        token = self.parse_authorization_token(request)
        user = self.jwt_user_from_token(token, self.claims)
        return user
