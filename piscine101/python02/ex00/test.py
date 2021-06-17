# class TestClass:
#     x = "test"

#     def test_method1(self):
#         print(self.x)

#     def test_method2(self, arg1):
#         print("argument1" + arg1)

# testClass = TestClass()
# testClass.test_method1()
# testClass.test_method2("argument test")


class Circle:
  def __init__(self, radius):
    # インスタンス変数に値を代入
    self.radius = radius
 
  # 関数を定義
  def area(self):
    return self.radius * self.radius * 3.14

r = 10
# インスタンスの生成
circle = Circle(r)

print("円の半径:", r)
print("円の面積:", circle.area())