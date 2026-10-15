import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-accessevent-2025-long-string")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///accessevent.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_HOURS = 24
