gameBoard = [["   "," 1 "," 2 "," 3 "," 4 ", " 5 "],
             [" 1 ","[D]","[ ]","[ ]","[ ]","[ ]"],
             [" 2 ","[D]","[ ]","[ ]","[ ]","[ ]"],
             [" 3 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 4 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 5 ","[ ]","[ ]","[ ]","[ ]","[ ]"]]
hitPoints = 2
shotsTaken = 0
displayBoard = [["   "," 1 "," 2 "," 3 "," 4 ", " 5 "],
             [" 1 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 2 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 3 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 4 ","[ ]","[ ]","[ ]","[ ]","[ ]"],
             [" 5 ","[ ]","[ ]","[ ]","[ ]","[ ]"]]
for i in displayBoard:
    print(*i)
print()

while(hitPoints != 0):
    shot = input("Enter a shot (r c): ")
    shotSplit = shot.split()
    shotsTaken += 1
    row = int(shotSplit[1])
    column = int(shotSplit[0])

    if (gameBoard[row][column] == "[D]"):
        displayBoard[row][column] = "[H]"
        hitPoints -= 1
        gameBoard[row][column] = "[H]"
        for i in displayBoard:
            print(*i)
        print("Well done you hit!")
    elif(gameBoard[row][column] == "[H]"):
        for i in displayBoard:
            print(*i)
        print("Already hit")
    else:
        displayBoard[row][column] = "[M]"
        for i in displayBoard:
            print(*i)
        print("Thats a miss!")
print("You win! \nIt took you {} shots".format(shotsTaken))