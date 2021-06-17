from beverage import Beverage

class Vendingmachine:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def __str__(self):
        tmp = self.name + " the vending machine."
        return tmp

    def sell(self, beverage_name):
        flag = 0
        for menber in self.stock:
            if beverage_name == menber.name:
                print(">You can buy " + str(beverage_name))
                flag = 1
        if flag == 0:
            print("You cannot buy " + str(beverage_name))


    def ask(self):
        print(">Please input drink name you want.")
        tmp = input()
        Vendingmachine.sell(self, tmp)



