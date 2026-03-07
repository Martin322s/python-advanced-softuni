def get_info(**kwargs):
    name = kwargs.get("name", "Unknown")
    town = kwargs.get("town", "Unknown")
    age = kwargs.get("age", "Unknown")
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))