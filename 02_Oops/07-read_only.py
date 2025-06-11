# Define a Car class
class Car:
    def __init__(self, brand, model): 
        # Public attribute: can be accessed and modified from outside
        self.brand = brand
        # Protected attribute (by convention): should not be accessed directly from outside
        self._model = model

    # Method to return the full name of the car
    def full_name(self):
        return f"{self.brand} {self._model}"
    
    @property  # Decorator to make a method act like a read-only attribute
    def model_for_read_only(self):
        # Only allows reading the value of _model, not modifying it
        return self._model

# Create an instance of Car
carObj1 = Car("Ferrari", "488 GTB")

# The following line creates a new public attribute 'model' on the instance,
# but it does NOT change the protected attribute '_model'.
carObj1.model = "city"

# This prints the value of the protected attribute '_model', which is still "488 GTB"
print(carObj1._model)

# If you try to assign to carObj1.model_for_read_only, it will raise an error:
# carObj1.model_for_read_only = "city"  # Uncommenting this will cause AttributeError

# Summary:
# - _model is a protected attribute (by convention, not enforced)
# - model_for_read_only is a read-only property for _model
# - Assigning carObj1.model = "city" does NOT change _model, it just adds a new attribute
