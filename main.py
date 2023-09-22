from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.base_config import Users
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from products.router import router as products_router

fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title='SFDiet'
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


app.include_router(products_router)
