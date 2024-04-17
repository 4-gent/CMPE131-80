from flask import Flask

app_obj = Flask(__name__)

from src import routes
