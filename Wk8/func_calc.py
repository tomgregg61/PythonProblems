print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")

choice = int(input("Please choose from one of the above functions: "))
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

def add(num1 = num1, num2 = num2):
    return num1 + num2

def subtract(num1 = num1, num2 = num2):
    return num1 - num2

def multiply(num1 = num1, num2 = num2):
    return num1 * num2

def divide(num1 = num1, num2 = num2):
    return num1 / num2

def remainder(num1 = num1, num2 = num2):
    return num1 % num2


if(choice == 1):
    print(add())
elif(choice == 2):
    print(subtract())
elif(choice == 3):
    print(multiply())
elif(choice == 4):
    print(divide())
elif(choice == 5):
    print(remainder())
else:
    print(exit())