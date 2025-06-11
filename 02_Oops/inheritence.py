class Car:

    def __init__(self, brand, model):  
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Electric_Car(Car): #make another class and add the ref in parentheses
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)   
        self.battery_size = battery_size


carObj1 = Electric_Car("Tesla", "Model S", 100)

print(carObj1.model)
print(carObj1.full_name())

