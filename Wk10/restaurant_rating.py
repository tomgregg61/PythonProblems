stars = {'1': 0,'2': 0, '3': 0, '4': 0, '5': 0}
exit = False
rating = -1
try:
     rating = int(input("Please enter a rating from 1-5 or -1 to exit: "))
except ValueError:
   print("Please enter a valid integer")
if (rating == -1):
    exit = True
elif (rating > 0 and rating < 5):
    stars[str(rating)] += 1
else:
    print("Integer not in range")
ratings = []
for star in stars:
        currentRating = star + ":"
        for i in range(stars[star]):
            currentRating += "-"
        ratings.append(currentRating)
while(exit == False):
    try:
     rating = int(input("Please enter a rating from 1-5 or -1 to exit: "))
    except ValueError:
        print("Please enter a valid integer")
    if (rating == -1):
        exit = True
    elif (rating > 0 and rating < 6):
        stars[str(rating)] += 1
    else:
        print("Integer not in range")
    ratings = []
    for star in stars:
            currentRating = star + "*:"
            for i in range(stars[star]):
                currentRating += "-"
            ratings.append(currentRating)
    ratings.reverse()

for i in ratings:
    print (i)

