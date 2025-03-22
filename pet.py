class Pet:
    name = ""
    age = 0
    healthpoints = 0
    healthstatus = ""
    species = ""

    def __init__(self, name, age, healthpoints, healthstatus,species):
        self.name = self.setName(name)
        self.age = self.setAge(age)
        self.healthpoints = self.setHealthPoints(healthpoints)
        self.healthstatus = self.setHealthStatus(healthpoints)
        self.species = self.setSpecies(species)
        
            
    def setName(self, newName):
        Pet.name = newName
    
    def setAge(self, newAge):
        Pet.age = newAge

    def setSpecies(self, newSpecies):
        Pet.species = newSpecies
    
    def setHealthPoints(self, newHealthpoints):
        Pet.healthpoints = newHealthpoints
    
    def setHealthStatus(self, healthpoints):
        if 76 <= healthpoints <= 100:
            Pet.healthstatus = "Great"
        elif 51 <= healthpoints <= 75:
            Pet.healthstatus = "Good"
        elif 26 <= healthpoints <= 50:
            Pet.healthstatus = "Fair"
        elif 1 <= healthpoints <= 25:
            Pet.healthstatus = "Bad"
        else:
            Pet.healthstatus = "Dead"

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
    

    
    
    
    