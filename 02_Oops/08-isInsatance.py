class Car:
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self): 
        return "Petrol or diesel"
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)   
        self.battery_size = battery_size
    def fuel_type(self): 
        return "Electric charge"    
         

#here we need to prove that carobj2 is an instance of a car too as we know its a instance of electric car
carObj2 = Electric_Car("Tesla", "Model S", 100)
print(isinstance(carObj2, Car))
print(isinstance(carObj2, Electric_Car))



