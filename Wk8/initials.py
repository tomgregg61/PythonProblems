name = input("Please enter your first name and family name: ")
names = name.split(' ')
firstName = names[0]
familyName = names[1]
initials = firstName[0] + "." + familyName[0]
print(initials)