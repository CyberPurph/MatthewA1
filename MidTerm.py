#Class

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Welcome to the computer store {self.username}"

class Product:
    def __init__(self, price, items, quantity, discount):
        self.price = price
        self.items = items
        self.quantity = quantity
        self.discount = discount

    def total(self):
        if self.discount == "Yes" or "YES" or "yes" or "y":
            total = (self.quantity * self.price) - self.discount
        else:
            total = (self.quantity * self.price)
        return total
        
    def __str__(self):    
        return f"Your order is as followed. You want {self.quantity} {self.price} , which are {self.items} each."

#Input

User_name = input("What is your username? ")

userItem = input("What are you trying to buy? ")
userPrice = input("How much is the item? ")
userQuantity = input("How many are you trying to buy? ")
userDiscount = input("Would you like to apply a discount? ")

#Objects

user = User(User_name)
product = Product(userItem, userPrice, userQuantity, userDiscount)

#Output

print(user)
print(product)