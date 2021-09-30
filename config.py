import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = '49e355ddf97e440aa449ec7bab6233bc'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    # SQLALCHEMY_BINDS = {
    #     'users': 'sqlite:///' + os.path.join(BASE_DIR, 'users.db')
    # }
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/db'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'tyavIgd9cQIzlWOjOgoNmSJCbQ406toA'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'artemgoh@gmail.com'
    MAIL_PASSWORD = 'mkbgsdiplssvcros'
    TWELVEDATA_API_KEY = '49e355ddf97e440aa449ec7bab6233bc'
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'media/')
