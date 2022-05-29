from flask import Flask, render_template
from App.Models.Plate import *
from App.Database.db import *
from flask import request
import os

template_dir = os.path.abspath('./Views/')

app = Flask(__name__,template_folder=template_dir,static_folder='./Content/')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plate/canDrive/",methods=['GET'])
def canDrive():
    plate, date, hour = request.args.get('plate'),request.args.get('date'),request.args.get('hour')
    plateObj = Plate(plate)
    for restriction in restrictions:
        rest = restriction.hasRetriction(plateObj.value)
        if rest:
            plateObj.restrictions.append(restriction.hasRetriction(plateObj.value))
    return {
        "plate": plateObj.value,
        "date": date,
        "time": hour,
        "canDrive": plateObj.canDrive(date,hour),
    }