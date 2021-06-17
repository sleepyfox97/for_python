# from salesperson import Circle

# #from A import B で　Aの中のBにアクセスするという意味．
# # インスタンスの生成
# circle = Circle(10)
# print("円の半径:", 10)
# print("円の面積:", circle.area())

from product import Product
from salesperson import Salesperson

#このfailがimportされても動作しないようにするためのif文がこれ
if __name__ == "__main__":
    p1 = Product()
    print(p1)
    print(Product())

    a = Salesperson()
    print(a)
    b = Salesperson.promote
    print(b)