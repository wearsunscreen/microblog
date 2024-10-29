import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from routes import pages

load_dotenv()

# Flask app factory, must be named 'create_app'.
def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    app.register_blueprint(pages)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.get_default_database(default="microblog")

    return app
