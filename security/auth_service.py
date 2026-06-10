from datetime import (
    datetime,
    timedelta,
    timezone
)

import jwt

from fastapi import (
    HTTPException,
    status
)

from app.config import settings


class AuthService:

    def create_access_token(
        self,
        username: str,
        role: str
    ):

        expire = (
            datetime.now(
                timezone.utc
            )
            + timedelta(
                minutes=settings.JWT_EXPIRATION_MINUTES
            )
        )

        payload = {

            "sub": username,

            "role": role,

            "exp": expire
        }

        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )

    def verify_token(
        self,
        token: str
    ):

        try:

            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[
                    settings.JWT_ALGORITHM
                ]
            )

            return payload

        except jwt.PyJWTError:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

    def authorize(
        self,
        token: str,
        allowed_roles: list
    ):

        payload = (
            self.verify_token(
                token
            )
        )

        role = payload.get(
            "role"
        )

        if role not in allowed_roles:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )

        return payload
