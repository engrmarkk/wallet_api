from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
app = Flask(__name__)
api = Api()
jwt = JWTManager()
