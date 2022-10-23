import datetime
import DataHandler

class Food:
    foodName = None
    dateBought = None
    dateExpiry = None
    amount = None
    units = None

    def __init__(self, name, dateBought, dateExpiry, amount, units):
        self.name = name
        self.dateBought = dateBought
        self.dateExpiry = dateExpiry
        self.amount = amount
        self.units = units

    def addToFood(self):
        database = DataHandler()
        database.addFood(self.foodName, self.units)
    
    def addToUserFood(self):
        database = DataHandler()
        database.addUserFood(self.foodID, self.dateBought, self.dateExpiry, self.amount)

    def getName():
        return self.foodName
