from flask import Flask
from flask_cors import CORS
from controller.usersResouce import users
from controller.categoryResource import categories
from controller.tagResource import tags
from controller.gameResource import games
from controller.orderResource import orders
import os
import time

db_user = 'postgres'
db_password = 'postgres'

# Update the database URI to use the service name 'postgres'
DATABASE_URI = os.environ.get('DATABASE_URI', f"postgresql://{db_user}:{db_password}@postgres:5432/practica")

def create_api():
    time.sleep(8) # Wait for the database to be ready
    api = Flask(__name__)
    api.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    cors = CORS(api)

    api.register_blueprint(users)
    api.register_blueprint(games)
    api.register_blueprint(orders)
    api.register_blueprint(categories)
    api.register_blueprint(tags)

    return api
