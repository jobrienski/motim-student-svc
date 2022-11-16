from typing import Any, AnyStr, Dict, Optional
from uuid import UUID

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class JWTUser(BaseModel):
    uid: UUID = None
    claims: Dict[AnyStr, Any] = {}

    def get_claim(self, key: AnyStr) -> Optional[Any]:
        return self.claims.get(key, None)
