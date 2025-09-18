import random

class MyList:
    def __init__(self, letters):
        self.mylist = letters

    def reversed_list(self):
        return self.mylist[::-1]

    def sorted_list(self):
        return sorted(self.mylist)

    def random_number_list(self):
        return [random.randint(0, 100) for _ in range(len(self.mylist))]

letters = ['a', 'c', 'b', 'e', 'd']
ml = MyList(letters)

print("Original list:", ml.mylist)
print("Reversed list:", ml.reversed_list())
print("Sorted list:", ml.sorted_list())
print("Random number list:", ml.random_number_list())
