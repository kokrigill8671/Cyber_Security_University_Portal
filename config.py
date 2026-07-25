
import os

class Config:

    SECRET_KEY = "CyberUniversityPortal2026"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "cyberportal_secret_key"

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "portal.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False