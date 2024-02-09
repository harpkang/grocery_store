class Product():
    def __init__(self, product_name=None, price=None, quantity=None):
        self.name=product_name
        self.price=price
        self.quantity=quantity
        
    def update_quantity(self,quantity):
        self.quantity+=quantity

class Customer(Product):
    def __init__(self,customer_name):
        super().__init__(product_name=None,price=None,quantity=None)
        self.name=customer_name
        self.cart={}
        
        
    def add_to_cart(self,Product, quantity):
        self.cart[Product]=quantity
        x=globals()[Product]
        x.update_quantity(-quantity)
        
        
    def remove_from_cart(self,Product, quantity):
        self.cart[Product]-=quantity
        if (Product in self.cart.keys()) and self.cart[Product]<=0:
            self.cart.pop('Product')
        x=globals()[Product]
        x.update_quantity(quantity)
    
    def checkout(self):
        total_sum=0
        for product, quantity in self.cart.items():
            total_sum+=(globals()[product].price*quantity)
        return total_sum
    
class Store(Product):
    
    def __init__(self):
        self.inventory=[]
    
    def add_product(self,Product):
        self.inventory.append(globals()[Product])
        
    def remove_product(self,Product):
        self.inventory.remove(globals()[Product])