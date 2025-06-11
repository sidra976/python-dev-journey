class Car:
    #first we make constructor
    def __init__(self, brand, model):  # self is like 'this' in JS
        self.__brand = brand # by add __ we make the attribute private 
        self.model = model
    def get_brand(self):
        return self.__brand + '!'    
    def full_name(self):
        return f"{self.__brand} {self.model}"
# now we make objects with car names
carObj1 = Car("Ferrari", "488 GTB")
# print(carObj1.__brand) #we cant access it directly the only way to access the brand name to use the function
print(carObj1.get_brand())

