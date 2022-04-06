class Customer:
    def __init__(self, input_name, input_wallet,input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunk_lvl = 0
        self.drinks = []

    def remove_money(self, price):
        self.wallet -= price

    def buy_drink(self, input_drink, input_pub):
        self.drinks.append(input_drink.name)
        self.drunk_lvl += input_drink.alcohol_level
        x = 0
        for check in input_pub.stock[input_drink.name]:
            if check == input_drink.name:
                self.drink += input_pub.stock[input_drink.name]
            print(self.drinks)
        # for drink in input_pub.stock:
        #     print(input_pub.stock)
        #     if drink == input_drink.name:
        #         print("hello")
        

    def buy_food(self, input_food):
        self.drunk_lvl -= input_food.reju_lvl
        
        #print(self.drunk_lvl)


        #self.drunk_lvl += 
        