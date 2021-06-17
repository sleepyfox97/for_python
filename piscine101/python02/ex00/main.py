from product import Product
from salesperson import Salesperson

if __name__ == "__main__":
    a = Product()
    print(a)
    b = Salesperson("42tokyo")
    print(b.promote())
