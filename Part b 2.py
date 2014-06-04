class Farmer:
    def __init__(self, name, number, farmer=None):
        self.setName(name)
        self.setNumber(number)
        self.setNextFarmer(farmer)
    def setName(self, name):
        self.name = name
    def setNumber(self, number):
        self.number = number
    def setNextFarmer(self, farmer):
        self.nextFarmer = farmer
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def getNextFarmer(self):
        return self.nextFarmer
class Village:
    def __init__(self, days, bags):
        self.days = days
        self.bags = bags
        self.first_farmer = None
        self.farmers = 0
        self.received = None
    def addFarmer(self, name):
        if self.first_farmer is None:
            new_farmer = Farmer(number=1,name=name)
            self.first_farmer = new_farmer
            self.farmers = self.farmers+1
        else:
            last_farmer = self.first_farmer
            while last_farmer.getNextFarmer() is not None:
               last_farmer = last_farmer.getNextFarmer()
            new_farmer = Farmer(number = last_farmer.getNumber()+1, name=name)
            last_farmer.setNextFarmer(new_farmer)
        self.farmers = self.farmers + 1
        
    def removeFarmer(self,number):
        previous_farmer = self.first_farmer
        while previous_farmer.getNextFarmer() is not None:
            each_farmer = previous_farmer.getNextFarmer()
            if each_farmer.getNumber() == number:
                previous_farmer.setNextFarmer(each_farmer.getNextFarmer())
                self.farmers = self.farmers-1
                print "removed farmer ", number
                return
            previous_farmer = each_farmer
        print "No farmer with that number!!"
    def printFarmers(self):
        farmer = self.first_farmer
        while farmer.getNextFarmer() is not None:
            print "Number: " ,farmer.getNumber(), " Name: ", farmer.getName()
            farmer = farmer.getNextFarmer()
            
    #set the last received, for now second farmer        
    def setReceived(self):
        self.received = self.first_farmer.getNextFarmer()
    def nextFarmer(self):
        return self.received.getNextFarmer().getNumber();
    def previousFarmer(self):
        previous = self.first_farmer
        while previous.getNextFarmer() is not None:
            farmer = previous.getNextFarmer()
            if farmer.getNumber() == self.received.getNumber():
                return previous
            previous = farmer
        print "No previous"
            
    

village = Village(bags=2,days=1)
village.addFarmer(name="John")
village.addFarmer(name="Peter")
village.addFarmer(name="Ken")
village.addFarmer(name="James")
village.addFarmer(name="Kenneth")
print "Farmer", village.first_farmer.getNextFarmer().getName()
village.printFarmers()
village.removeFarmer(2)
village.addFarmer(name="Tim")
village.printFarmers()
village.setReceived()
print "Next Farmer ", village.nextFarmer()
print "Previous Farmer ", village.previousFarmer().getNumber()

    
    
