from flask import Flask
import Models
import Database.db as db
from Models.Restriction import Restriction
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"