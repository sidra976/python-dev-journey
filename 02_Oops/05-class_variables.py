class Car:
    total_cars = 0 #making varaible in car 
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
        Car.total_cars+=1

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
carObj3 = Electric_Car("Tesla", "Model S", 100)
#we can also make objects without storing it into other var like
Car("McLaren", "720S")


print(Car.total_cars)

