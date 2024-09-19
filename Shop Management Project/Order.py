from Shop import Shop
from Product import Product

class Order:
    def __init__(self):
        self.choosedProducts = {} #Stores products like ['productName' = 'quantity'] format.

    def addToCart(self, shopName, productName, quantity):
        product = shopName.findProduct(productName)
        if product:
            if product.quantity < quantity:
                print(f"\nSorry! Only {product.quantity} pieces of {productName} is available!")
            else:
                remainingQuantity = product.quantity - quantity #calculates new quantity.
                price = product.price
                productName = product.name
                shopName.deleteProduct(product) # deletes the product having details.
                shopName.addProduct(Product(productName,remainingQuantity,price)) # adds the product with updated details.
                self.choosedProducts[productName] = quantity # added to the customer cart.
                print(f"\n{quantity} amounts of {productName} are added in the cart!")
        else:
            print(f"\nSorry!! {productName} was not found.")

    def removeFromCart(self, shopName, productName):
        product = shopName.findProduct(productName)
        if product:
            newQuantity = product.quantity + self.choosedProducts[productName] #calculates new quantity.
            newProduct = Product(productName,newQuantity,product.price) # creates the same product to insert it in the list.
            
            self.choosedProducts.pop(productName) # removes product from cart.

            shopName.deleteProduct(product) # deletes the product having details.
            shopName.addProduct(newProduct) # adds the product with updated details.

            print(f"\n{productName} was removed form the cart!")
        else:
            print(f"\nSorry!! {productName} was not found.")

    def calcualteBill(self,shopName):
        total = 0
        for productName in self.choosedProducts:
            product = shopName.findProduct(productName)
            total += (product.price*self.choosedProducts[productName])
        return total
    
    def viewCart(self,shopName):
        print("\nProducts ---- Quantity ---- Price")
        for productName, quantity in self.choosedProducts.items():
            product = shopName.findProduct(productName)
            print(f"{productName} ---- {quantity} ---- {product.price}")
        print(f"--> Total Bill: {self.calcualteBill(shopName)}")