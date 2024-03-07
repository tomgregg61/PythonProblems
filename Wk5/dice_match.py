import random

match = False
rollsTilMatch = 1
while match == False:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Dice 1 has rolled:", dice1)
    print("Dice 2 has rolled:", dice2)
    if dice2 == dice1:
        print("Match found!")
        print("Rolls until match:", rollsTilMatch)
        match = True
    else: 
        print("No match found, rolling again")
        rollsTilMatch += 1