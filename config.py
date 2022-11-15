import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
        set config vars for the flask app using enviorment vars where available
        otherwise create the config var if not done already
    """
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SERCRET_KEY') or 'Moto is a good boy'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlit:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False