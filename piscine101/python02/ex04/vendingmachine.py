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
        while True:
            tmp = random.choice(self.stock)
            if tmp[1] > 0:
                break
        print(">" + tmp[0].name + " is very delicious, so I recommend it.")
        #print(random.choice(self.stock.name))

    def __str__(self):
        tmp = self.name + " the vending machine."
        return tmp

    def sell(self, beverage_name):
        flag = 0
        for i in range(len(self.stock)):
            if beverage_name == self.stock[i][0].name and self.stock[i][1] > 0:
                print(">You can buy " + str(beverage_name))
                self.stock[i][1]-=1
                flag = 1
        if flag == 0:
            print(">sorry, there is no " + beverage_name)
            Vendingmachine.recommend(self)
        else:
            print(">Do you want to buy?\nPress \"y\" or \"n\"")
            while True:
                tmp = input()
                if tmp == 'y':
                    print(">You get it.")
                    break
                elif tmp == 'n':
                    print(">Choose other drink.")
                    break
                else:
                    print(">You have to press \"y\" or \"n\"")

    def add_stock(self, beverage_name, number):
        flag = 0
        for i in range(len(self.stock)):
            if beverage_name == self.stock[i][0].name:
                self.stock[i][1] += number
                flag = 1
        if flag == 0:
            tmp = Beverage(str(beverage_name), 42, "42", "42")
            self.stock.append([tmp, number])


    def ask(self):
        print(">enter drink name you want!")
        tmp = input()
        Vendingmachine.sell(self, tmp)



