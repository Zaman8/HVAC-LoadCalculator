#initial global/building wide variables
global rWall, rWindow
rWall = 21
rWindow = 1
Zones = []
buildingload = 0

class Zone: #create class Zone with variables for each potiental heat load influencer
    
    heatload=0
    Area = 0
    wallSA = []
    tempDif = []
    windowSA = []
    wtempDif = []
    Persons = 0
    machineWatt = []

    def calHeatLoad(self): #calculate heat load of the entire zone
            heatload = self.Area
            for i in range(len(self.wallSA)):
                heatload+=(int(self.wallSA[i]) * int(self.tempDif[i]))/rWall
            for i in range(len(self.windowSA)):
                heatload+=(int(self.windowSA[i]) * int(self.wtempDif[i]))/rWindow
            heatload+=int(self.Persons)*600
            intMachineWatts = map(int, self.machineWatt) #convert strings in machineWatt to list of ints 
            heatload+=sum(intMachineWatts)*3.4
            return heatload
    
    def __init__(self, Area, wallSA, tempDif, windowSA, wtempDif, Persons, machineWatt): #initialize each variable to data from txt file
        self.Area = Area
        self.wallSA = wallSA
        self.tempDif = tempDif
        self.windowSA = windowSA
        self.wtempDif = wtempDif
        self.Persons = Persons
        self.machineWatt = machineWatt
        self.heatload = self.calHeatLoad()
      


    def getHeatLoad(self): #accessor for heatload (not needed but want to protect variable)
           return self.heatload





try:
    data = open('data.txt', 'r').read().splitlines() #open data txt file and parse in as seperate lines
except FileNotFoundError:
    print("File \"data.txt\" not found \nCheck that file exists and is in same folder")
    input()
    exit()


for i in range(len(data)):
    if data[i][:4] == "Zone": #find start of each Zone section
        Zones.append(Zone(int(data[i+2])*int(data[i+4]), data[i+6].split(","), data[i+8].split(','), data[i+10].split(','), data[i+12].split(','), data[i+14], data[i+16].split(',') ))


for i in Zones:
    buildingload += i.getHeatLoad()

print("Estimated Heating Load is " + str(int(buildingload)) + " BTU/hr");
print("\nHeat Load for Zones:")
for i in Zones:
    j=1
    print("Zone " + str(j) + ": " + str(int(i.getHeatLoad())))

input()





