import os

class Config:
    SECRET_KEY = os.environ.get('b50d5a669754b63f30c125fa535328f1') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SENDGRID_API_KEY = os.environ.get('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')
