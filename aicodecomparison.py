# Manual Implementation
def sort_dict_list(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

# AI-Generated Implementation (e.g., from Copilot)
def sort_by_key(dicts, key):
    dicts.sort(key=lambda d: d.get(key))
    return dicts

# Sample data
people = [
    {"name": "Alice", "age": 32},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 29}
]

# Run both versions
print("Manual:", sort_dict_list(people, "age"))
print("AI     :", sort_by_key(people.copy(), "age"))