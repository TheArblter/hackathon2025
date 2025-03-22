class Budgeter:
    savingsTotal = 0
    spentTotal = 0
    savingsGoal = 0

    def __init__(self,savingsTotal,spentTotal, goal):
        self.savingsTotal = self.setSavings(savingsTotal)
        self.spentTotal = self.setSpent(spentTotal)
        self.goal = self.setGoal(goal)
    
    def setSavings(self, newSaved):
        Budgeter.savingsTotal += newSaved

    def getSavings(self):
        return Budgeter.savingsTotal
    
    def setSpent(self, newSpent):
        Budgeter.savingsTotal += newSpent

    def getSavings(self):
        return Budgeter.savingsTotal
    
    def setGoal(self, newGoal):
        Budgeter.goal = newGoal
        
    def getGoal(self):
        return Budgeter.savingsTotal
    


    
    


