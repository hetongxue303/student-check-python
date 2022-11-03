from typing import Optional, List

from pydantic import BaseModel


class Token(BaseModel):
    """ token """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
