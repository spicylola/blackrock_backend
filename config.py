import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('POST_URL')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:TMBlackRockBackEnd@blackrocktaskmanager.c0uikdugnayd.us-east-1.rds.amazonaws.com:5432/TaskManagerDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
