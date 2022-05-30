from flask import Flask, render_template, abort, request
from App.Models.Plate import *
from App.Database import db
from datetime import datetime
import os

from App.Models.Restriction import Restriction

template_dir = os.path.abspath('./Views/')
print(template_dir)


def create_app(test_config=None):
    app = Flask(__name__,template_folder='./Views/',static_folder='./Content/')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/plate/canDrive/",methods=['GET'])
    def canDrive():
        dbContext = db.get_db()
        dbContext.row_factory = lambda cursor, row: Restriction(row[0],row[1],row[2],row[3])
        restrictions = dbContext.execute(
            'SELECT dayOfWeek,regexExpression,initTime,endTime'
            ' FROM restriction'
        ).fetchall()
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
    db.init_app(app)
    return app

def canDriveIsValid(date, time, plate):
    try:
        datetime.strptime(date, '%d-%m-%Y').weekday()
        datetime.strptime(time,'%H:%M')
        return True and plate.isValid()
    except Exception as e:
        print(e)
        return False

app = create_app()