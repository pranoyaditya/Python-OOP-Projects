from Product import Product

class Shop:
    def __init__(self,shopName):
        self.shopName = shopName
        self.productList = [] # List to store products.
        self.sellerList = [] #List to store seller objects.
        self.customerList = [] #List to store customer objects.

    def addProduct(self, product):
        self.productList.append(product)

    def findProduct(self, productName):
        for product in self.productList:
            if product.name.lower() == productName.lower():
                return product
            
    def addCustomer(self,customer):
        self.customerList.append(customer)
        print(f"\nCongratulations {customer.name}! Your account has been created.")

    def addSeller(self,seller):
        self.sellerList.append(seller)
        print(f"\n{seller.name} was added as a seller.")

    def deleteProduct(self, product):
        self.productList.remove(product)  

    def showProducts(self):
        print("\nProducts ---- Quantity ---- Price")
        for product in self.productList:
            print(f"{product.name} ---- {product.quantity} ---- {product.price}")

    def verifyCustomer(self,email,password):
        for customer in self.customerList:
            if customer.email == email and customer.password == password:
                return customer
    
    def verifySeller(self,email,password):
        for seller in self.sellerList:
            if seller.email == email and seller.password == password:
                return seller
