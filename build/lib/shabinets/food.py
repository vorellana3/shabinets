import datetime

class Food:
    foodID = 0
    dateBought = datetime.datetime(0, 0, 0)
    dateExpiry = datetime.datetime(0, 0, 0)
    amount = 0.0

    def __init__(self, foodID, dateBought, dateExpiry, amount):
        self.foodID = foodID
        self.dateBought = dateBought
        self.dateExpiry = dateExpiry
        self.amount = amount



    

