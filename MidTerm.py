#Class

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Thank you for ordering {self.username}"

class Product:
    def __init__(self, price, items, quantity):
        self.price = price
        self.items = items
        self.quantity = quantity
        
    def __str__(self):    
        return f"Your order is as followed. You want {self.quantity} {self.price} , which are {self.items} each."

#Input

User_name = input("What is your username? ")

while True:

    userItem = str(input("What are you trying to buy? "))
    userPrice = float(input("How much is the item? "))
    userQuantity = int(input("How many are you trying to buy? "))
    userDiscount = str(input("Would you like to apply a discount? "))
    userContinue = str(input("Would you like anything else? "))

    if userContinue == "No" or "NO" or "no" or "n":
        break
    elif userContinue == "Yes" or "YES" or "yes" or "y":
        print("Please enter what else you would like")

#Objects

user = User(User_name)
product = Product(userItem, userPrice, userQuantity)

#Total

total = (userPrice * userQuantity)
if userDiscount == "Yes" or "yes" or "y" or "YES":
    total = (userPrice * userQuantity) * 0.9
else:
    print(total)

#Output

print(user)
print(product)
print("Your total is $", total)