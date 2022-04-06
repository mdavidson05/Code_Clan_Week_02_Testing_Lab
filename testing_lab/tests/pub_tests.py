import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Stuart", 100, 18)
        self.drink =  Drink("Jack Daniels", 1.50, 3)
        self.pub = Pub("Prancing Pony", 1000, {"Jack Daniels": [10, 1.50], 
        "Baileys": [20, 2],
         "Beer" : [30, 1]
        })
        
        # for total in self.pub.stock[total][0]:

        #     current_stock += total
        # print(current_stock)
        


    def test_money_added_to_till(self):
        self.pub.add_money(self.drink.price)
        self.assertEqual(1001.50, self.pub.till)

    def test_check_customer_age(self):
        self.pub.customer_age(self.customer.age)

    def test_check_customer_alcohol_level(self):
        self.pub.customer_drunkness(self.customer.drunk_lvl)
            # break

    # def test_stock_check(self):
    #     #print(self.pub.stock)
    #     self.customer.buy_drink(self.drink,self.pub)
        #self.pub.stock_check(self.pub.stock)
        # self.pub.stock_check()
        #print(self.pub)
        