import re
class Plate:  
    def __init__(self, value):
        self.value = value
        self.restrictions = []

    def canDrive(self,date,time):
        for restriction in self.restrictions:
            if not restriction.canDrive(date,time):
                return False
        return True
    
    def isValid(self):
        if re.search("^[a-zA-Z]{3}[0-9]{4}$",self.value):
            return True
        return False