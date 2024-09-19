from Person import Person,Seller,Customer
from Shop import Shop
from Product import Product
from Order import Order

#shop object.
Goriber_Dukan = Shop("Goriber Dukan")

#Customer fucntion.
def customerFunction(customer):
    while True:
        print("\n----------Welcome to customer Page----------")
        print("\n1. View product list.")
        print("2. Buy a product.")
        print("3. Remove a product from cart.")
        print("4. View your cart.")
        print('5. Pay the bill.')
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            customer.seeProducts(Goriber_Dukan)
        elif choice == '2':
            productName = input("\nEnter product name: ")
            quantity = int(input("Enter quantity: "))
            customer.buyProduct(Goriber_Dukan, productName, quantity)
        elif choice == '3':
            productName = input("\nEnter product name: ")
            customer.removeProduct(Goriber_Dukan, productName)
        elif choice == '4':
            customer.viewCart(Goriber_Dukan)
        elif choice == '5':
            amount = int(input("Enter your money amount: "))
            customer.payBill(Goriber_Dukan, amount)
        elif choice == '6':
            break
        else:
            print("Wrong input! Choose again.")

#Log in fucntion.
def logIn():
    print("\n---> Please Login.")
    print("\n1. As Customer.")
    print("2. As Seller.")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        email = input("Enter email: ")
        password = input("Enter password: ")

        customer =  Goriber_Dukan.verifyCustomer(email,password)
        
        if customer:
            customerFunction(customer)
        else:
            print("\n-----> No customer found!")
        return
    elif choice == '2':
        email = input("Enter email: ")
        password = input("Enter password: ")

        seller =  Goriber_Dukan.verifySeller(email,password)
        
        if seller:
            sellerFunction(seller)
        else:
            print("\n-----> No seller found!")
        return
    
#Seller function.
def sellerFunction(seller):
    while True:
        print("\n----------Welcome to Seller Page----------")
        print("\n1. Add a product.")
        print("2. Remove a product.")
        print("3. View products.")
        print("4. Find a product.")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            productName = input("\nEnter product name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter product price: "))

            product = Product(productName, quantity, price)

            seller.addProduct(Goriber_Dukan,product)
            print(f"\n{product.name} with {product.quantity} quantity was added successfully!!")
        elif choice == '2':
            productName = input("\nEnter product name: ")
            product = Goriber_Dukan.findProduct(productName)
            if product:
                seller.deleteProduct(Goriber_Dukan, product)
                print(f"\n{productName} was removed successfully!")
            else:
                print(f"\nSorry!!{productName} was not found.")
            
        elif choice == '3':
            seller.seeProducts(Goriber_Dukan)
        elif choice == '4':
            productName = input("\nEnter product name: ")
            seller.findProduct(Goriber_Dukan, productName)
        elif choice == '5':
            break
        else:
            print("Wrong input! Choose again.")


#Main function.
while True:
    print("\n---------Main Page---------")
    print("\n1. Sign Up as a Customer")
    print("2. Sign Up as a Seller.")
    print("3. Login")
    print("4. Exit the store.")

    choice = input("Enter your choice: ")

    if choice == '1':
        customerName = input("Enter your name: ")
        customerEmail = input("Enter your email: ")
        customerPass = input("Enter your password: ")

        # creating customer object.
        customer = Customer(customerName, customerEmail)
        customer.password = customerPass

        #adding the customer in the shop database.
        Goriber_Dukan.addCustomer(customer)

        #Goes to login page.
        logIn()
    elif choice == '2':
        sellerName = input("Enter your name: ")
        sellerEmail = input("Enter your email: ")
        sellerPass = input("Enter your password: ")

        #creating seller object.
        seller = Seller(sellerName, sellerEmail)
        seller.password = sellerPass

        #adding the seller in the shop database.
        Goriber_Dukan.addSeller(seller)

        #Goes to login page.
        logIn()
    elif choice == '3':
        logIn()
    elif choice == '4':
        print(f"\nThanks for using {Goriber_Dukan.shopName} shop!!\n")
        break
    else:
        print("\nWrong input! Choose again.")
