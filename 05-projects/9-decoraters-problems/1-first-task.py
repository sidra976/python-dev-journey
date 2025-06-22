# Problem 1: Add a Welcome Message Before a Function Runs


def say_welcome(func):
     def wrapper():
          print('Welcome')
          func()
     return wrapper

@say_welcome
def greet():
    print('Good to see you')

greet()


        

     
