def set_budget():
    global budget
    budget = float(input("Enter your budget: "))
    print(f"Your Budget is: {budget}")

def add_items(items):    
    item = input("Enter item you want to shop: ").strip().title()
    price = float(input("Enter price of item per unit: "))
    quantity = int(input("Enter quantity: "))
    items[item] = (quantity, price)

def view_items(items):
    if not items:
        print("Please add Items!")
    else: 
        for index , (item, (quantity, price)) in enumerate(items.items()):
            print(f"{index + 1}. {item} {quantity} {price} = {quantity * price}")
def remove_items(items):
    delete = input("Enter item you want to delete: ").strip().title()
    for item in items:
        if  delete not in item:
            print('Item not in list')
    if delete in items:
        del items[delete]

def calculate_total(items):
    total = sum(qnty * price for qnty, price in items.values())
    print(f"Your total is: {total}")
    rem = budget - total
    print(f"Your balance is: {rem}")
    if total > budget:
        print("You're beyond the set budget")
    else:
        print('You are still within budget')

def apply_discount(items):
    item = input("Enter the item on discount: ").strip().title()
    if item not in items:
        print(f"{item} does not exist in list")
    else:
        discount = float(input("Enter discount in %: "))
        quantity, price = items[item] 
        new_price = price - (price * discount/100)
        items[item ] = (quantity, new_price)    


