strings = []

for i in range(5):
    choice = input("Please enter a string: ")
    strings += [choice]
alphabetically = sorted(strings)

for i in range(len(alphabetically)):
    print(alphabetically[i])