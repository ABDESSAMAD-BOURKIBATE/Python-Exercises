class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(member)

members_list = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
my_family = Family("Smith", members_list)
my_family.family_presentation()
my_family.born(name="Tom", age=0, gender="Male", is_child=True)
my_family.family_presentation()
