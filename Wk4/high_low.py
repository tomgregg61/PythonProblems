import random
def drawCard():
    card = ""
    lol = []
    value = random.randint(1,13)
    lol.append(value)
    if (value == 1):
        card = "Ace"
    elif(value > 1 and value < 11):
        card = str(value)
    elif(value == 11):
        card = "Jack"
    elif(value == 12):
        card = "Queen"
    elif(value == 13):
        card = "King"
    lol.append(card)
    return lol
pick1 = drawCard()
guess = input("First card drawn is {} do you think next draw will be higher or lower [higher / lower]: ".format(pick1[1]))
pick2 = drawCard()
print("Second card drawn is {}".format(pick2[1]))
if(guess == "higher" and pick2[0] > pick1[0]):
    print("Correct you win")
elif(guess == "lower" and pick2[0] < pick1[0]):
    print("Correct you win")
else:
    print("Incorrect you lose")