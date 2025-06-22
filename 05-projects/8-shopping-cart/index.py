import json
import os

FILE_NAME = 'cart.json'

def total_amount(cart):
    total = sum(price['Price'] for price in cart)
    print(f'Total Amount: {total}')

def view_cart(cart):
    if not cart:
        print('Cart is empty')
    else:
        for index, userItem in enumerate(cart , start=1):
          print(f'{index}- {userItem['Item']}, Price: {userItem['Price']}$')
          

def add_items(cart):
    item = input('Add the item: ')
    price = int(input('Add price: '))
    cart.append({'Item' : item, 'Price' : price})
    save_items(cart)
    print(f'{item} added Succesfully!')

def delete_items(cart):
    if not cart:
        print('Cart is empty')
    else:
     view_cart(cart)
    try:
      choice = int(input('Enter index of item: '))
      if 1 <= choice <= len(cart):
          removed = cart.pop(choice - 1)
          save_items(cart)
          print(f"Deleted: {removed['Item']} | Amount: {removed['Price']}")
      else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def save_items(cart):
    with open(FILE_NAME, 'w') as file:
        json.dump(cart,file)


def load_cart():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return []


cart = load_cart()
while True:
    print('\nTo-Do List')
    print('1. View Cart')
    print('2. Add Items In Cart')
    print('3. Delete Item From Cart')
    print('4. View total amounr')
    print('5. Exit')
    choice = input('Enter your choice: ')
    match choice:
        case '1':
            view_cart(cart)
        case '2':
            add_items(cart)
        case '3':
            delete_items(cart)
        case '4':
            total_amount(cart)
        case '5':
            print("Exiting. Goodbye!")
            break
        case _:
            print('Invalid choice')
