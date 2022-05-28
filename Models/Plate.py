class Plate:  
    def __init__(self, value):
        self.value = value
        self.restrictions = []

    def canDrive(self):
        for restriction in self.restrictions:
            if not restriction.canDrive():
                return False
        return True
    def isValid(self,value):
        return False