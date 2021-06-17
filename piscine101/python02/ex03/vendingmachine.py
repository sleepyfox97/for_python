from beverage import Beverage
import random

class Vendingmachine:
    def __init__(self, name, greeting, stock):
        self.name = name
        self.stock = stock
        self.greeting = greeting

    def greet(self):
        print(str(self.greeting))

    def deisplay(self):
        for menber in self.stock:
            print(str(menber.name))
    
    def recommend(self):
        tmp = random.choice(self.stock)
        print(tmp.name + " is very delicious, so I recommend it.")
        #print(random.choice(self.stock.name))

    def __str__(self):
        tmp = self.name + " the vending machine."
        return tmp

    def sell(self, beverage_name):
        for menber in self.stock:
            if beverage_name == menber.name:
                tmp1 =  "You can buy " + str(beverage_name)
                print(tmp1)
                return
        Vendingmachine.recommend(self)


    def ask(self):
        tmp = input()
        Vendingmachine.sell(self, tmp)



