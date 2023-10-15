

class Bulb:
    status = False

    def isOn(self):
        self.status = True
    
    def isOff(self):
        self.status = False

    def getStatus(self):
        if self.status == True:
            return "Bulb is glowing"
        elif self.status == False:
            return "Bulb is not glowing"
        else:
            pass
