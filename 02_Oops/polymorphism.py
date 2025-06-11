class Car:
    
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self): #Polymorphism
        return "Petrol or diesel"
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)   
        self.battery_size = battery_size
    def fuel_type(self): #Polymorphism
        return "Electric charge"    
         

carObj1 = Car("Ferrari", "488 GTB")
carObj2 = Electric_Car("Tesla", "Model S", 100)

print(carObj1.fuel_type())
print(carObj2.fuel_type())

