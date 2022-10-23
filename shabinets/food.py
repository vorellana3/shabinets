import datetime
import json

class Food:
    name = ""
    dateBought = datetime.date(2022, 10, 20)
    dateExpiry = datetime.date(2022, 10, 22)
    amount = 0.0

    def __init__(self, name, dateBought, dateExpiry, amount):
        self.name = name
        self.dateBought = dateBought
        self.dateExpiry = dateExpiry
        self.amount = amount

    def addToUserFood(self):
        database = DataHandler()
        database.addUserFood(self.foodID, self.dateBought, self.dateExpiry, self.amount)

def getUpcomingExpiryDates():
    #vivien: get top 10 expiry dates form database, replace below line, array of food objects
    foods = [Food("bacon", datetime.date(2022, 10, 20), datetime.date(2022, 10, 24), 1)]
    foods_json = {}
    for food in foods:
        foods_json[food.name] = (food.dateExpiry).strftime('%m/%d/%Y')
    return json.dumps(foods_json)

def getExpiredFoods():
    #vivien: iterate through database items
    foods = [Food("bacon", datetime.date(2022, 10, 20), datetime.date(2022, 10, 24), 1),
             Food("tomato", datetime.date(2022, 10, 20), datetime.date(2022, 10, 22), 1)]
    expiredFoods = {}
    for food in foods:
        if food.dateExpiry < datetime.date.today():
            expiredFoods[food.name] = (food.dateExpiry).strftime('%m/%d/%Y')
    return json.dumps(expiredFoods)

