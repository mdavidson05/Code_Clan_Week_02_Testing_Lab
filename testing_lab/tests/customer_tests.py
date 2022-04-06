import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Stuart", 100, 18)
        self.drink =  Drink("Jack Daniels", 1.50, 3)
        self.pub = Pub("Prancing Pony", 1000)
    
    def test_customer_has_name(self):
        self.assertEqual("Stuart", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)
    
    def test_customer_has_enough_money(self):
        self.customer.remove_money(self.drink.price)
        self.customer.wallet >= self.drink.price
    

    def test_customer_buys_drink(self): #We could replace list with dictionary and minues stock form pub for each transaction
        self.customer.buy_drink(self.drink)
        self.assertEqual(1, len(self.customer.drinks))

#Review this concept
    def test_customer_orders_drink(self):
        self.customer.buy_drink(self.drink)
        #print(self.customer.drinks)
        self.customer.remove_money(self.drink.price)
        #print(self.customer.wallet)
        self.pub.add_money(self.drink.price)
        #print(self.pub.till)

    


