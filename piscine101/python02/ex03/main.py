from product import Product
from beverage import Beverage
from vendingmachine import Vendingmachine

if __name__ == "__main__":
    p1 = Product("apple", 100, "This is a red fluit." )
    print(p1)
    print(p1.print_attr())

    coke = Beverage("coke", 200, "This is coke.", "cold")
    print(coke.print_attr())

    water = Beverage("water", 100, "This is water.", "cold")
    coffee = Beverage("coffee", 150, "This is coffer.", "hot")

    vending = [coke, water, coffee]

    p = Vendingmachine("tokyo", "Hello" ,vending)
    print(p)

    p.ask()
    while True:
        print("Do you want buy this? Press \"y\" or \"n\"")
        tmp = input()
        if tmp == 'y':
            break
        #else if tmp != 'n'
            #print("You should press \"y\" or \"n\"")
            


    #for member in vending:
     #   print("name:", member.name)
