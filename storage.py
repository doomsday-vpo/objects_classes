# Create a class Storage. The __init__ method should accept one parameter - the capacity of the storage.
# The Storage class should also have an attribute called storage - empty list, where all the items will be stored.
# The class should have two additional methods:
# •	add_product(product: str) - adds the product in the storage if there is enough space for it
# •	get_products() - returns the storage list

class Storage:
    storage = []
     def __init__(self, capacity):
        self.capacity = capacity


