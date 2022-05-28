import datetime
import re

class Restriction:
    def __init__(self, dayOfWeek, regexExpression,initTime, endTime):
        self.dayOfWeek = dayOfWeek
        self.regexExpression = regexExpression
        self.initTime = initTime
        self.endTime = endTime

    def canDrive(self,date, time):
        if self.isWithinDay(date) and self.isWithinHour(time):
            return False
        return True

    def isWithinDay(self, date):
        print("This is executed")
        return datetime.strptime(date, '%d/%m/%y').weekday() == self.dayOfWeek   

    def isWithinHour(self, time):
        print("This is not executed")
        return (datetime.strptime(time,'%H/%M') >= datetime.strptime( self.initTime,'%H/%M') and datetime.strptime(time,'%H/%M') <= datetime.strptime( self.endTime,'%H/%M'))  

    def hasRetriction(self, plate):
        if re.search(self.regexExpression, plate):
            return self
        return None