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

userItem = str(input("What are you trying to buy? "))

trueprice = 0

while True:

    userPrice = float(input("How much is the item? "))
    if trueprice < userPrice:
        break
    else:
        userPrice = print("Please enter a price above 0 ")
        
truequantity = 0

while True:

    userQuantity = int(input("How many are you trying to buy? "))
    if truequantity < userQuantity:
        break
    else:
        userQuantity = print("Please enter a number above 0")

userDiscount = str(input("Would you like to apply a discount? (y/n)"))

userContinue = str(input("Would you like anything else? (y/n)"))
        

#Objects

user = User(User_name)
product = Product(userItem, userPrice, userQuantity)

#Total

totaldiscount = (userPrice * userQuantity) * 0.9

totalnormal = (userPrice * userQuantity)
    

#Output

print(user)
print(product)

if userDiscount == "y":
    print("Your total is $", totaldiscount)
else:
    print("Your total is $", totalnormal)