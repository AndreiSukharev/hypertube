import os


class Config:
    DEBUG = True
    SECRET_KEY = b'supersecretkey'
    # SESSION_TYPE = 'filesystem'
    JWT_SECRET_KEY = 'dude this is a very terrible key'
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    JWT_BLACKLIST_ENABLED = True
    UPLOAD_FOLDER = '/usr/src/backend/videos_hub'


mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": os.environ['EMAIL_USER'],
        "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}
