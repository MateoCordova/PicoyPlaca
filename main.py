from flask import Flask
from Models import Plate
import Database.db as db
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/canDrive")
def canDrive(plate, date, hour):
    plateObj = Plate(plate)
    for restriction in db.restrictions:
        plateObj.restrictions.add(restriction.hasRetriction())