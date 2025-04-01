class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity: int):
        if self.stock + quantity < 0:
            print("Error: Insufficient stock!")
        else:
            self.stock += quantity
            print("Stock updated successfully!")
    
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"

def main():
    products = {}
    print("\n$$$ STOCK MANAGEMENT $$$")
    while True:
        print("\n1. Add Product")
        print("2. Update Stock")
        print("3. View Product Details")
        print("4. Exit")
        print()
        choice = input("Enter your choice: ")
        print()
        #ADD Product
        if choice == "1":
            name = input("Enter product name:\t  ").strip()
            try:
                price = float(input("Enter product price: \t "))
                stock = int(input("Enter product stock: \t "))
                if price < 0 or stock < 0:
                    print("Error: Price and stock must be non-negative!")
                else:
                    products[name] = Product(name, price, stock)
                    print("\n $$$Product added successfully!$$$")
            except ValueError:
                print("!!!Invalid input! Please enter valid numeric values.!!!")
            #Update Stock
        elif choice == "2":
            name = input("Enter product name to update:\t ").strip()
            if name in products:
                try:
                    quantity = int(input("Enter quantity to add/remove: \t"))
                    products[name].update_stock(quantity)
                except ValueError:
                    print("$$$Invalid input! Please enter a valid integer.$$$")
            else:
                print("!!!Product not found!!!")
            #view Details
        elif choice == "3":
            name = input("Enter product name: \t").strip()
            if name in products:
                print(products[name])
            else:
                print("!!!Product not found!!!")
            #exits
        elif choice == "4":
            print("\n$$$Exiting the system. Goodbye!$$$ :)")
            break
        
        else:
            print("!!!Invalid choice! Please try again.!!!")
            
if __name__ == "__main__":
    main()
