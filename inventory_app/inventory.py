from inventory_app.models import Product  # Import the Product model

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, quantity, price):
        if id not in self.products:
            self.products[id] = Product(id=id, name=name, quantity=quantity, price=price)
            return True
        return False

    def update_quantity(self, id, quantity):
        if id in self.products:
            self.products[id].quantity = quantity
            return True
        return False

    def get_product(self, id):
        return self.products.get(id)

    def remove_product(self, id):
        if id in self.products:
            del self.products[id]
            return True
        return False

    def list_products(self):
        return [
            {
                'id': product.id,
                'name': product.name,
                'quantity': product.quantity,
                'price': product.price
            }
            for product in self.products.values()
        ]

    def get_total_inventory_value(self):
        return sum(product.quantity * product.price for product in self.products.values())