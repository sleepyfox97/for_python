from product import Product
from beverage import Beverage


if __name__ == "__main__":
    p1 = Product("Juice", 100, "This is apple juice." )
    print(p1)
    print(p1.print_attr())

    p2 = Beverage("coke", 200, "Thi is famous drink.", "cool")
    print(p2.print_attr())
