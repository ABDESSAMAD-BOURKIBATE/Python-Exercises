class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        for animal in sorted_animals:
            letter = animal[0].upper()
            if letter not in grouped_animals:
                grouped_animals[letter] = []
            grouped_animals[letter].append(animal)
        return grouped_animals

    def get_groups(self):
        groups = self.sort_animals()
        for letter, group in groups.items():
            print(f"{letter}: {group if len(group) > 1 else group[0]}")

# Example usage
new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Ape")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()
new_york_zoo.get_groups()
