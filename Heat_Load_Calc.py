#initial global/building wide variables
global rWall, rWindow, levelHeight
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
            heatload = self.Area * 31.25
            for i in range(len(self.wallSA)):
                heatload+=(self.wallSA[i] * self.tempDif[i])/rWall
            for i in range(len(self.windowSA)):
                heatload+=(self.windowSA[i] * self.wtempDif[i])/rWindow
            heatload+=int(self.Persons)*600
            heatload+=sum(self.machineWatt)*3.4
            return heatload
    
    def __init__(self, Area, wallLengths, tempDif, windowSA, wtempDif, Persons, machineWatt): #initialize each variable to data from txt file
        self.Area = Area
        self.wallSA = list(map(lambda x: x*levelHeight, map(int, wallLengths))) #multply each wall length by the height of the level to get SA
        self.tempDif = list(map(int, tempDif)) #convert wall temps to ints
        self.windowSA =  list(map(int, windowSA)) #convert window SA to list of ints
        self.wtempDif = list(map(int, wtempDif)) #convert window temps to ints
        self.Persons = Persons
        self.machineWatt = list(map(int, machineWatt)) #convert machine watts to ints
        self.heatload = self.calHeatLoad()
      


    def getHeatLoad(self): #accessor for heatload (not needed but want to protect variable)
           return self.heatload





try:
    data = open('data.txt', 'r').read().splitlines() #open data txt file and parse in as seperate lines
except FileNotFoundError:
    print("File \"data.txt\" not found \nCheck that file exists and is in same folder")
    input()
    exit()

rWall=int(data[1]) #assign global values
rWindow=int(data[3]) #placement is hard coded from data.txt
levelHeight=int(data[5])

for i in range(len(data)):
    if data[i][:4] == "Zone": #find start of each Zone section
        #print(data[i+6].split(','))
        Zones.append(Zone(int(data[i+2])*int(data[i+4]), data[i+6].split(','), data[i+8].split(','), data[i+10].split(','), data[i+12].split(','), data[i+14], data[i+16].split(',') ))
        #enter all data to create a new Zone, will automaticaly call calHeatLoad at end of init

for i in Zones:
    buildingload += i.getHeatLoad()

print("Estimated Heating Load is " + str(int(buildingload)) + " BTU/hr");
print("\nHeat Load for Zones:")
j=1
for i in Zones:
    print("Zone " + str(j) + ": " + str(int(i.getHeatLoad())))
    j+=1

input()





