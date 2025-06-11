class Car:
    #first we make constructor
    def __init__(self, brand, model):  # self is like 'this' in JS
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
# now we make objects with car names
carObj1 = Car("McLaren", "720S")
carObj2 = Car("Rolls Royce", "Phantom")

print(carObj1.brand)
print(carObj1.model)
print(carObj1.full_name())
print(carObj2.brand)
print(carObj2.model)
