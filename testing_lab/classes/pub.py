class Pub:
    def __init__(self, input_name, input_till, input_stock):
        self.name = input_name
        self.till = input_till
        self.stock = input_stock 
        

    def add_money(self, price):
        self.till += price

    def customer_age(self, input_age):
        if input_age < 18:
            print('Not tonight m8')
            #break

    def customer_drunkness(self, input_alcohol_level):
        if input_alcohol_level >= 10:
            print("You're cut off m8")
            #break

    #def stock_check(self): dictionary with multiple key value pairs