
import os

class Config:

    SECRET_KEY = "CyberUniversityPortal2026"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/cyber_portal"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

=======
import os
class Config:

    SECRET_KEY = "CyberUniversityPortal2026"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/cyber_portal"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "static/uploads"