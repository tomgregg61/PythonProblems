cands = {"Alex": 0, "Joe": 0, "Sam": 0, "Tyler": 0, "Evie": 0}
stopPlaying = False

def makeVote():
    vote = input("Please make your vote from candidates [Alex, Joe, Sam, Tyler, Evie]: ")
    cands[vote] += 1

makeVote()

ordered = sorted(cands.keys(), key=lambda x: (-cands[x], x))

print("1. {}\n2. {}\n3. {}\n4. {}\n5. {}".format(*ordered))

cont = input("Press 1 to end voting or nothing to continue: ")

if cont == "1":
    stopPlaying = True

while not stopPlaying:
    makeVote()
    ordered = sorted(cands.keys(), key=lambda x: (-cands[x], x))
    
    print("1. {}\n2. {}\n3. {}\n4. {}\n5. {}".format(*ordered))
    
    cont = input("Press 1 to end voting or nothing to continue: ")
    
    if cont == "1":
        stopPlaying = True

ordered = sorted(cands.keys(), key=lambda x: (-cands[x], x))

print(cands)
print(ordered)
print("The winner is {}!".format(ordered[0]))
