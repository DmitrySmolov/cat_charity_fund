from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд (0.1.0)'
    app_description: str = (
        'Фонд собирает пожертвования на различные целевые проекты: на '
        'медицинское обслуживание нуждающихся хвостатых, на обустройство '
        'кошачьей колонии в подвале, на корм оставшимся без попечения кошкам '
        '— на любые цели, связанные с поддержкой кошачьей популяции.'
    )
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()


class Constant:
    JWT_TOKEN_URL = 'auth/jwt/login'
    JWT_TOKEN_LIFETIME = 3600
    JWT_AUTH_BACKEND_NAME = 'jwt'
    USER_PASSWORD_MIN_LEN = 3


class Message:
    USER_PASSWORD_TOO_SHORT = (
        f'Пароль не должен быть короче {Constant.USER_PASSWORD_MIN_LEN} '
        'символов.'
    )
    USER_PASSWORD_IS_EMAIL = 'Пароль не должен совпадать с емейлом.'
    USER_REGISTRED = 'Зарегистрирован пользователь:'
    USER_DELETE_NOT_ALLOWED = 'Удаление пользователей запрещено!'
