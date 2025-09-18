class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"{name} added to menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish.update({"price": price, "spice": spice, "gluten": gluten})
                print(f"{name} updated in menu.")
                return
        print(f"{name} not found in menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} removed from menu.")
                print("Updated menu:", self.menu)
                return
        print(f"{name} not found in menu.")

manager = MenuManager()
manager.add_item("Pizza", 20, "A", True)
manager.update_item("Salad", 20, "B", False)
manager.remove_item("Soup")
