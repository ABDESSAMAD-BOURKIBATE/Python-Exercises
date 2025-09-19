import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if 1 <= page_num <= self.total_pages:
            self.current_idx = page_num - 1
        else:
            raise ValueError(f"Page {page_num} is out of range. Available pages: 1-{self.total_pages}.")
        return self  

    def first_page(self):
        self.current_idx = 0
        return self  

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self  
    
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self  

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self  

    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(str(item) for item in visible_items)



alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("Page 1:", p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print("Page 2:", p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print("Last Page:", p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print("Error:", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("Error:", e)

print("\nCurrent Page Display:")
print(p)
