from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from database.mysql import get_db
from sqlalchemy.orm import Session

router = APIRouter()
