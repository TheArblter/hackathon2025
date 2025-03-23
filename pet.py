class Pet:
    name = ""
    age = 0
    healthpoints = 0
    healthstatus = ""
    species = ""

    def __init__(self, name, age, healthpoints, healthstatus, species):
        self.name = self.setName(name)
        self.age = self.setAge(age)
        self.healthpoints = self.setHealthPoints(healthpoints)
        self.healthstatus = self.setHealthStatus(healthpoints)
        self.species = self.setSpecies(species)
        
            
    def setName(self, newName):
        Pet.name = newName
    
    def setAge(self, newAge):
        Pet.age = newAge
    
    def setHealthPoints(self, newHealthpoints):
        Pet.healthpoints = newHealthpoints
    
    def setHealthStatus(self, healthpoints):
        #n = 0
        #while (100, 75, 50, 25, 0)[n] >= healthpoints:
           #n += 1
        Pet.healthstatus = ("Great", "Good", "Fair", "Bad", "Dead")[4 - int(healthpoints/25)] # Change index to n and uncomment all previous code if this doesn't work; The commented code is a little bit less flashy, but it works

    def getName(self):
        return Pet.name
    
    def getAge(self):
        return Pet.age
    
    def getSpecies(self):
        return Pet.species
    
    def getHealthPoints(self):
        return Pet.healthpoints
    
    def getHealthStatus(self):
        return Pet.healthstatus
    

    
    
    
    