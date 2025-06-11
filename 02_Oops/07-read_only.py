class Car:
    def __init__(self, brand, model): 
        self.brand = brand
        self._model = model

    def full_name(self):
        return f"{self.brand} {self._model}"
    
    @property #known as decorater
    def model_for_read_only(self):
        return self._model


carObj1 = Car("Ferrari", "488 GTB")
# #if we changed the model name we can easily do that thats why we make the var private and make methods
# carObj1.model = "city"

# print(carObj1.model) #we r getting city but we dont want that anyone can change that 

carObj1.model = "city"
# print(carObj1.model) by using @property we cant change the attribute name
print(carObj1._model)

    
    



