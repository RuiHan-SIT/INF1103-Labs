class Inventory:
    def __init__(self):
        self.__inventory = []

    def add_product(self, product):
        self.__inventory.append(product)

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------------------------------------------------------")
        for product in self.__inventory:
            product.display_information()
        print("------------------------------------------------------------------------------------------------")

    def search_product(self, id):
        for product in self.__inventory:
            if id == product.get_id():
                return product
        return None

    def get_products(self):
        return self.__inventory