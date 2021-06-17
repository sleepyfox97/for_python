from product import Product
from beverage import Beverage
from vendingmachine import Vendingmachine

if __name__ == "__main__":
    p1 = Product("apple", 100, "This is a red fluit." )

    coke = Beverage("coke", 200, "This is coke.", "cold")

    water = Beverage("water", 100, "This is water.", "cold")
    coffee = Beverage("coffee", 150, "This is coffer.", "hot")

    vending = [coke, water, coffee]

    p = Vendingmachine("tokyo", vending)
    print(p)
    flag = 1
    while True:
        if flag == 1:
            p.ask()
        print("Do you want to continue? Press \"y\" or \"n\"")
        tmp = str(input())
        if tmp == 'y':
            flag = 1
            continue
        elif tmp == 'n':
            break
        else:
            flag = 0
            continue
