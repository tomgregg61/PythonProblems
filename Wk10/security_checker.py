import json
import re

json_file_path = '/Users/thomas/Documents/programming/UniSofDev/Wk10/users.json'

def create_account():
    username = input("Enter your username: ")
    validPass = False
    while(not validPass):
        password = input("Enter your password: ")
        if (len(password) > 7 and bool(re.search(r"\s", password)) == False and password[0].isnumeric() == False):
            validPass = True
            confirm_password = input("Re-enter your password to confirm: ")
            if password == confirm_password:
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
                data[username] = password
                with open(json_file_path, 'w') as file:
                    json.dump(data, file)
                print("Account created successfully!")
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Invalid password try again")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

   
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    if username in data and data[username] == password:
        print("Welcome {}!".format(username))
    else:
        print("Invalid username or password. Please try again.")

user_choice = input("Select an option: 1. Create a new account, 2. Login\n")

if user_choice == '1':
    create_account()
elif user_choice == '2':
    login()
else:
    print("Invalid choice. Please select 1 or 2.")
