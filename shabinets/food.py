import datetime
import DataHandler

class Food:
    foodID = None
    foodName = None
    dateBought = None
    dateExpiry = None
    amount = None

    def __init__(self, name, foodID, dateBought, dateExpiry, amount):
        self.name = name
        self.foodID = foodID
        self.dateBought = dateBought
        self.dateExpiry = dateExpiry
        self.amount = amount

    def addToFood(self):
        database = DataHandler()
        database.addFood()

    def addToUserFood(self):
        database = DataHandler()
        database.addUserFood(self.foodID, self.dateBought, self.dateExpiry, self.amount)