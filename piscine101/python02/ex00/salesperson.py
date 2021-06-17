# class Circle:
#   def __init__(self, radius):
#     # インスタンス変数に値を代入
#     self.radius = radius
 
#   # 関数を定義
#   def area(self):
#     return self.radius * self.radius * 3.14
# __str__は特殊メソッドの一つ

from product import Product

class Salesperson:
    def __init__(self, name='nameless saleperson'):
        """
        assign its value to a name attribute.
        """
        self.name = name

    def __str__(self):
        """
        return name attribute of the instance.
        """
        return self.name

    def promote(self):
        """
        return a Product instance.
        """
        return Product()




