
tries = 0
rows, cols = (4,4)
display = [["*" for i in range(cols)] for j in range(rows)]
temp = [["*" for i in range(cols)] for j in range(rows)]
matchesNeeded = 8

def showDeck():
    for rows in display:
      for cols in rows:
         print(cols,end = " ")
      print()

cards = {"0 0": "King", "0 1": "Jack", "0 2": "Jack", "0 3": "Ace", "1 0": "Queen", "1 1": "King", "1 2": "Jack", "1 3": "Ace", "2 0": "Queen", "2 1": "Queen", "2 2": "King", "2 3": "Ace", "3 0": "Queen", "3 1": "Ace", "3 2": "King", "3 3": "Jack"}
chosen = []

def pickCard():
   position = choice.split()
   row = int(position[0])
   col = int(position[1])
   display[row][col] = "X"
   print()



while matchesNeeded != 0:
   validChoices = False
   
   def checkIfChosen(display = display):
    global validChoices
    for i in range(len(chosen)):
        if (chosen[i] == choice):
            print("Already matched")
            showDeck()
            validChoices = False
            return True


   while not validChoices:
      validChoices = True
      choice = input("Please enter position of card you would like to pick: ")
      pickCard()
      print("The card you selected is a {}".format(cards[choice]))
      if checkIfChosen():
         display = [row[:] for row in temp]
         continue
      choice1 = cards[choice]
      coord1 = choice
      showDeck()

      choice = input("Please enter position of second card to pick: ")
      pickCard()
      print("The second card you selected is {}".format(cards[choice]))
      choice2 = cards[choice]
      coord2 = choice
      if checkIfChosen():
         display = [row[:] for row in temp]
      showDeck()
   
   tries += 1
   if (choice1 == choice2 and coord1 != coord2):
      print("Match found")
      matchesNeeded -= 1
      temp = [row[:] for row in display]  
      chosen.append(coord1)
      chosen.append(coord2)
   else:
      print("No match")
      display = [row[:] for row in temp]
      showDeck()
print ("Congratulations you matched all the pairs")
print("It took %s attempts" % tries)