#assumptions
class Farmer:
    def __init__(self, number, name):
        self.setNumber(number)
        self.setName(name)
    def setNumber(self,number):
        self.number = number
    def setName(self, name):
        self.name = name
    def getNumber(self):
        return self.number
    def getName(self):
        return self.name
class Village:
    def __init__(self,bags,days):
        self.bags = bags
        self.days = days
        self.farmers = []
        self.number_of_farmers = 0
        self.received = 3
    def addFarmer(self, name):
        if self.number_of_farmers > 0:
            new_farmer = Farmer(number = self.farmers[self.number_of_farmers-1].getNumber()+1, name=name)
        else:
            new_farmer = Farmer(number=1, name=name)
        self.farmers.append(new_farmer)
        self.number_of_farmers = self.number_of_farmers+1
        print "Added farmer ", new_farmer.getNumber()
        
    def removeFarmer(self,number):
        for each_farmer in self.farmers:
            if each_farmer.getNumber() == number:
                self.farmers.remove(each_farmer)
                self.number_of_farmers = self.number_of_farmers-1
                #for each_farmer in self.farmers:
                 #   each_farmer.number = number--
                print "Removed farmer ", number
                return
        print "No farmer with that number!!"
    def printFarmers(self):
        for each_farmer in self.farmers:
            print "Number: " ,each_farmer.getNumber(), " Name: ", each_farmer.getName()
    def nextFarmer(self):
        n=1
        for each_farmer in self.farmers:
            if each_farmer.getNumber() == self.received:
                return self.farmers[n].getNumber()
            n = n+1
        return 0
    def previousFarmer(self):
        n=1
        for each_farmer in self.farmers:
            if each_farmer.getNumber() == self.received:
                return self.farmers[n-2].getNumber()
            n = n+1
        return 0
    
    def xDays(self, days):
        n=1
        skip = days/self.days
        for each_farmer in self.farmers:
            if each_farmer.getNumber() == self.received:
                return self.farmers[n+skip-1].getNumber()
            n = n+1
        return 0
            
village = Village(bags=2,days=1)
village.addFarmer(name="John")
village.printFarmers()
village.addFarmer(name="Njoroge")
village.addFarmer(name="Kamau")
village.addFarmer(name="Koech")
village.printFarmers()
village.removeFarmer(number=2)
village.printFarmers()
village.addFarmer(name="Tonui")
village.printFarmers()
print "next ",village.nextFarmer()
print "previous ", village.previousFarmer()
print "xDays", village.xDays(2)
        
