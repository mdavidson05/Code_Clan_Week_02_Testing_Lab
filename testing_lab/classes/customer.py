class Customer:
    def __init__(self, input_name, input_wallet,input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunk_lvl = 0
        self.drinks = []

    def remove_money(self, price):
        self.wallet -= price

    def buy_drink(self, input_drink):
        self.drinks.append(input_drink)
        self.drunk_lvl += input_drink.alcohol_level


        #self.drunk_lvl += 
        