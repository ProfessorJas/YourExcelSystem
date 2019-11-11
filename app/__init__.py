from flask import Flask     # import Flask object from flask package
from config import Config
from flask_bootstrap import Bootstrap

import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

from flask_moment import Moment

app = Flask(__name__)       # assign the Flask object to the variabel app
app.config.from_object(Config)

# Add bootstrap to prettify the page
bootstrap = Bootstrap(app)

# add moment to change the timezone
moment = Moment(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

if not app.debug:


    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors      # import routes from app package
