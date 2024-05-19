from pydantic import BaseModel, ConfigDict, EmailStr, validator


MIN_LENGTH_PASSWORD = 8


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str

    @validator('password')
    def validate_password_complexity(cls, value):
        if len(value) < MIN_LENGTH_PASSWORD:
            raise ValueError(f'Пароль должен содержать не менее {MIN_LENGTH_PASSWORD} символов')

        if not any(char.isdigit() for char in value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

        if not any(char.isupper() for char in value):
            raise ValueError('Пароль должен содержать хотя бы одну букву в верхнем регистре')

        if not any(char.islower() for char in value):
            raise ValueError('Пароль должен содержать хотя бы одну букву в нижнем регистре')

        return value


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
