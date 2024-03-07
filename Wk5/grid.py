column = int(input("Please enter number of columns: "))
row = int(input("Please enter number of rows: "))
for i in range(row):
    output = "* "
    for i in range(column - 1):
        output = output + "* "
    print(output)
