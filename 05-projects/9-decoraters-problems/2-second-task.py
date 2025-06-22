def decorator_(func):
    def wrapper(*args, **kwargs):  
        print('Your sum is done')
        return func(*args, **kwargs)  
    return wrapper

@decorator_
def sum(a, b):
    return a + b

add = sum(2, 3)
print(add)
