from product import Product

class Beverage(Product):
    def __init__(self, name, price, description, temperature):
        super().__init__(name, price, description,)
        self.temperature = temperature

    def print_attr(self):
        tmp = "name : " + str(self.name) + "\nprince : " + str(self.price) + "\ndesciption : " + str(self.description)+"\ntmperature : " + str(self.temperature)
        return tmp
