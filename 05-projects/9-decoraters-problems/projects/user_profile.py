is_logged_in = True
def login_required(func):
    count = 0
    def wrapper():
        if is_logged_in == True:
            nonlocal count
            print('You are allowed to access our db')
            func()
            count+=1
            print('Times a logged-in user', count)
        else:
            print('Access Denied')
    return wrapper

@login_required
def profile():
    print("User profile page")

profile()
profile()
profile()
