from flask import Flask     # import Flask object from flask package

app = Flask(__name__)       # assign the Flask object to the variabel app

from app import routes      # import routes from app package
