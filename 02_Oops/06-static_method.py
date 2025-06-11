class Car:
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod #also known as decoraters we dont use self if we use static method
    def general_desc():
        return "Cars are means of transport" 
    

print(Car.general_desc()) #static method we use when we dont want anyone to access the object

