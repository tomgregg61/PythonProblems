rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

choice = int(input("Please enter a number between 1-7 to pick a colour in the rainbow or -1 to exit: "))

exit = False
if choice == -1:
    exit = True
while not exit:
    print(rainbow[choice - 1])
    choice = int(input("Please enter a number between 1-7 to pick a colour in the rainbow or -1 to exit: "))
    if choice == -1:
        exit = True