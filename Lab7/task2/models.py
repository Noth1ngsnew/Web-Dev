class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= quantity

    def is_available(self):
        return self.stock > 0
    
    def get_stock(self):
        return self.stock
    
    def __str__ (self):
        return f"Product name: {self.name} | Price: {self.price:.2f} | Stock: {self.stock}" 
    
class Laptop(Product):
    def __init__(self, name, price, stock, brand, storage):
        super().__init__(name, price, stock)
        self.brand = brand
        self.storage = storage
        
    def upgrade_storage(self, extra_gb):
        self.storage += extra_gb
        return f"Storage upgraded to {self.storage}GB"
    
    def sell(self, quantity):
        super().sell(quantity)                        
        return f"{quantity} Laptop(s) sold! Remaining stock: {self.stock}"
    
    def __str__(self):
        base = super().__str__()                      
        return f"{base} | Brand: {self.brand} | Storage: {self.storage}GB"
     

class Smartphone(Product):
    def __init__(self, name, price, stock, color, battery_capacity):
        super().__init__(name, price, stock)
        self.color = color
        self.battery_capacity = battery_capacity

    def working_hours(self):
        return self.battery_capacity // 90
    
    def restock(self, quantity):
        super().restock(quantity)
        return f"{quantity} Smartphone(s) restocked! Total stock: {self.stock}"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} | Color: {self.color} | Battery: {self.battery_capacity}mAh"
    
