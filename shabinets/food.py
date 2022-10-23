import datetime

class Food:
    name = ""
    foodID = 0
    dateBought = datetime.datetime(2022, 10, 20)
    dateExpiry = datetime.datetime(2022, 10, 22)
    amount = 0.0

    def __init__(self, name, foodID, dateBought, dateExpiry, amount):
        self.name = name
        self.foodID = foodID
        self.dateBought = dateBought
        self.dateExpiry = dateExpiry
        self.amount = amount


<<<<<<< Updated upstream

    

||||||| constructed merge base
    def addToUserFood(self):
        database = DataHandler()
        database.addUserFood(self.foodID, self.dateBought, self.dateExpiry, self.amount)
=======
    def addToUserFood(self):
        database = DataHandler()
        database.addUserFood(self.foodID, self.dateBought, self.dateExpiry, self.amount)
>>>>>>> Stashed changes
