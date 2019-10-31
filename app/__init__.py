from flask import Flask     # import Flask object from flask package
from config import Config

app = Flask(__name__)       # assign the Flask object to the variabel app
app.config.from_object(Config)

from app import routes      # import routes from app package
