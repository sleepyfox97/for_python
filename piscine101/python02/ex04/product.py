class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        tmp = self.name + " : " + self.description
        return tmp
    
    def print_attr(self):
        tmp = 'name : '  + str(self.name) + '\nprice : ' + str(self.price) + '\ndescription : ' + str(self.description)
        return tmp
