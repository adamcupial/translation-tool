# this python file uses the following encoding utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('translation_tool.config')
db = SQLAlchemy(app)

from translation_tool import views, models
