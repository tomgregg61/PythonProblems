import json

# Read JSON data from a file
with open('/Users/thomas/Documents/programming/UniSofDev/Wk10/char_classes.json', 'r') as file:
    data = json.loads(file.read())

# Print header
print("{:<12} {:<5} {:<5} {:<5} {:<5} {:<5}".format("Class", "Str", "Int", "Wis", "Dex", "Con"))

# Print data in tabular format
for char_class, stats in data.items():
    print("{:<12} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
        char_class, stats["str"], stats["int"], stats["wis"], stats["dex"], stats["con"]
    ))