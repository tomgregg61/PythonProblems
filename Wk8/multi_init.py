
name = input("Enter a name: ")
words = name.split()
initials = ""
for word in words:
    if "-" in word:
        hyphen_parts = word.split("-")
        initials += ".".join(part[0].upper() + "-" for part in hyphen_parts[:-1]) + hyphen_parts[-1][0].upper() + "."
    else:
        initials += word[0].upper() + "."
print("Initials:", initials)
