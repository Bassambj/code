## COPYRIGHTS:
# © Airbus 2022
# ALL pertinents copyrights.

#Flypy
# PYTHON OOP AND FLYPY PROJECT...

class Aircraft:
    def __init__(self,name,manufact,weight,engine,trusth,fuelcp,passen,crewcp,speedx,speedl):
        self.name=name # name
        self.manufact=manufact # manufacturer
        self.weight=weight # weight in lbs
        self.engine=engine # engine type
        self.trusth=trusth # total trusth of engines
        self.fuelcp=fuelcp # aircraft fuel capacity in lbs
        self.passen=passen # passengers capacity
        self.crewcp=crewcp # crew capacity
        self.speedx=speedx # speed status
        self.speedl=speedl # aircraft limit speed - nm

    def speedup(self):
        self.speedx = self.speedx+20

    def speedow(self):
        self.speedx = self.speedx-20

    def fleetAircraft(self):
        print("\nId:  Manufacturer: ")
        print(self.name,self.manufact)
        print("Specifications:\nWeight:",self.weight,"lbs ","Engines:",self.engine,"Trusth:",self.trusth)
        print("Capabilities:\nFuel - ",self.fuelcp,"lbs\nPassengers - ",self.passen,"\nCrew - ",self.crewcp,"\nSpeed Limit - ",self.speedl,"nm")

    def speedTest(self):
        print("\n### SPEED TEST ###")
        print("=========================")
        print("  ",self.name,"= speed UP: ")                   
        while (self.speedx  < self.speedl):
            self.speedup()
            print(self.speedx," knots")
        print("Limit:",self.speedl,"<")
        print("=========================")
        print("  ",self.name,"= slowing DOWN: ")
        print("Airbus A319 slowing down: ")
        while (self.speedx > 0):
            self.speedow()
            print(self.speedx,"knots")

# Creating instances of the aircraft class:
a319 = Aircraft("A319","Airbus",129600.0,"PW1100G",66000,6280,160,5,0,400)
a320 = Aircraft("A320","Airbus",138400.0,"PW1100G",66000,6280,180,5,0,380)
a330 = Aircraft("A330","Airbus",138400.0,"PW4000",136000,25765,277,5,0,480)

print("Aircraft Flight Project")
a330.fleetAircraft()
a330.speedTest()

# Instances of aircraft prefixes
a320232 = a320()
PRMAG = a320232
PRMAK = a320232
PRMBA = a320232
PRMBF = a320232
LYMLN = a320232





















## COPYRIGHTS:
# © Airbus 2022
# ALL pertinents copyrights.