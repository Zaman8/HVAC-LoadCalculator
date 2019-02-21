
global rWall, rWindow
rWall = 21
rWindow = 1
Zones = []
buildingload = 0

data = open("data.txt", 'r').read().splitlines()
for i in range(len(data)):
    if data[i][:]

for i in Zones:
    buildingload+= getHeatLoad

print("Estimated Heating Load is " + buildingload);

class Zone:
      heatload=0
      Area = 0
      wallSA = []
      tempDif = []
      windowSA = []
      wtempDif = []
      Persons = 0
      machineWatt = []
      def calHeatLoad():
            heatload += Area
            for i in range(len(wallSA)):
                heatload+=(wallSA[i] * tempDif[i])/rWall
            for i in range(len(windowSA)):
                heatload+=(windowSA[i] * wtempDif[i])/rWindow
            heatload+=Persons*600
            heatload+=sum(machineWatt)*3.4
      def getHeatLoad():
           return heatload

