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
    NAME_FLD_MIN_LEN = 1
    NAME_FLD_MAX_LEN = 100
    CHARITY_ENDPOINTS_PREFIX = '/charity_project'
    CHARITY_ENDPOINTS_TAGS = ('charity_projects',)


class Message:
    USER_PASSWORD_TOO_SHORT = (
        f'Пароль не должен быть короче {Constant.USER_PASSWORD_MIN_LEN} '
        'символов.'
    )
    USER_PASSWORD_IS_EMAIL = 'Пароль не должен совпадать с емейлом.'
    USER_REGISTRED = 'Зарегистрирован пользователь:'
    USER_DELETE_NOT_ALLOWED = 'Удаление пользователей запрещено!'
    INVESTMENT_ERROR = 'В процессе распределения средств произошла ошибка.'
    CHARITY_DATES_ERROR = 'Дата закрытия не может быть раньше даты открытия.'
    CHARITY_AMOUNTS_ERROR = 'Внесённая сумма не может превышать полную сумму.'
    CHARITY_FUTURE_CREATE_ERROR = 'Дата открытия не может быть в будущем.'
    CHARITY_PROJ_NAME_EXISTS = 'Проект с таким именем уже существует.'
    CHARITY_PROJ_NAME_NOT_NULL = 'Название проекта не может быть пустым.'
    CHARITY_PROJ_DESCR_NOT_NULL = 'Описание проекта не может быть пустым.'
    CHARITY_PROJ_NOT_FOUND = 'Проекта с таким ID не найдено.'
    CHARITY_PROJ_INVESTED = 'В проект уже внесены средства. Удаление запрещено.'
    CHARITY_PROJ_CLOSED = 'Проект закрыт. Его редактирование запрещено.'
