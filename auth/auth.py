from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import sec_key

cookie_transport = CookieTransport(cookie_name='sfdiet', cookie_max_age=36000)

SECRET = sec_key


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=36000)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
