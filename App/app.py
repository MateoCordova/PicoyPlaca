from flask import Flask, render_template, abort, request
from App.Models.Plate import *
from App.Database.db import *
from datetime import datetime
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
    if canDriveIsValid(date,hour, plateObj):
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
    else:
        abort(400)

def canDriveIsValid(date, time, plate):
    try:
        datetime.strptime(date, '%d-%m-%Y').weekday()
        datetime.strptime(time,'%H:%M')
        return True and plate.isValid()
    except Exception as e:
        print(e)
        return False