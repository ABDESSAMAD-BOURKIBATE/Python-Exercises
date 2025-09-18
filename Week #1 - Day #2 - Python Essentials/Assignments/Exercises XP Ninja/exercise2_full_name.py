def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"

# أمثلة
print(get_full_name("john", "lee", "hooker"))
print(get_full_name("bruce", "lee"))
