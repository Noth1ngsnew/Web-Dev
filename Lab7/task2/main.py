from models import Product, Laptop, Smartphone

p = Product("T-Shirt", 3000, 200)
l = Laptop("MacBook Air M2", 500000, 500, "Apple", 512)
s = Smartphone("Redmi Note 9S", 50000, 100, "Blue", 3600)

products = [p, l, s]

print("ALL PRODUCTS\n")
for product in products:
    print(product)

print("\nMETHODS\n")

#Product Methods
print(f"Before restock: {p.get_stock()}")
p.restock(10)
print(f"After restock: {p.get_stock()}")
p.sell(20)
print(f"After sell: {p.get_stock()}")
print(f"Is available? : {p.is_available()}")

#Laptop Methods
print()
print(l.sell(2))
print(l.upgrade_storage(256))
print(f"Laptop available? : {l.is_available()}")

#Smartphone Methods
print()
print(s.restock(5))                
print(f"Working hours : {s.working_hours()} hrs")  
print(f"Phone available? : {s.is_available()}")  





