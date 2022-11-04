# from datetime import timedelta
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from starlette import status
# from core.security import authenticate_user, create_token
# from models import User
# from schemas.token import Token
#
# router = APIRouter()
#
#
# @router.post('/login', response_model=Token)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user: User = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = create_token(data={"sub": user.username}, expires_time=timedelta(minutes=30))
#     return {"access_token": access_token, "token_type": "Bearer"}
