width = int(input("Please enter width: "))

# centre = int(width // 2)
stars = "* "
gapCount = (width // 2) + 2
for i in range (width):
    line = " "
    for i in range(gapCount):
        line += " "
    line = line + stars
    print(line)
    gapCount -= 1
    stars = stars + "* "

# for i in range (width):
#     print("* ", end="")
#     print()
gapCount = 0
stars = stars[:-2]

for i in range(width):
    line = " "
    for i in range(gapCount + 1):
        line += " "
    stars = stars[:-2]
    line = line + stars
    print(line)
    gapCount += 1