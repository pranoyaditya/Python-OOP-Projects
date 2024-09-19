from Shop import Shop
from Order import Order

class Person:
    def __init__(self,name):
        self.name = name

#Seller class
class Seller(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.__passWord = None

    def addProduct(self, shopName, product):
        shopName.addProduct(product)

    def deleteProduct(self, shopName, productName):
        shopName.deleteProduct(productName)

    def findProduct(self, shopName, productName):
        product = shopName.findProduct(productName)
        if product:
            print(f"\n{productName} is in stock!.")
        else:
            print(f"\nSorry!!{productName} was not found.")
    
    def seeProducts(self,shopName):
        shopName.showProducts()
    
    @property
    def password(self):
        return self.__passWord
    
    @password.setter
    def password(self,passWord):
        self.__passWord = passWord


#Customer class
class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.__passWord = None
        self.cart = Order()

    def payBill(self, shopName, amount):
        totalBill = self.cart.calcualteBill(shopName)
        if amount < totalBill:
            print(f"\nSorry! You need to pay {totalBill} taka.")
        elif amount == totalBill:
            print("\nThanks for shopping here. Hava a nice day!")
        else:
            print(f"Here is your change: {amount - totalBill} taka.")
            print("\nThanks for shopping here. Hava a nice day!")
            

    def removeProduct(self, shopName, productName):
        self.cart.removeFromCart(shopName,productName)

    def buyProduct(self,shopName, productName, quantity):
        self.cart.addToCart(shopName,productName, quantity)

    def seeProducts(self,shopName):
        shopName.showProducts()

    def viewCart(self,shopName):
        self.cart.viewCart(shopName)

    @property
    def password(self):
        return self.__passWord
    
    @password.setter
    def password(self, passWord):
        self.__passWord = passWord