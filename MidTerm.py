#Class

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Welcome to the computer store {self.username}"

class Product:
    def __init__(self, price, items, discount):
        self.price = price
        self.items = items
        self.discount = discount

    def total(self):
        if self.discount == "Yes" or "YES" or "yes" or "y":
            total = (items * price) - discount
        else:
            total = (items * price)
        return total



#Input

User_name = input("What is your username? ")

#Objects

user = User(User_name)

#Output

print(user)