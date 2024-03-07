import random

winner = False
botScore = 0
userScore = 0
while winner == False:
    choiceUser = input("Please make a choice between rock, paper or scissors:").lower()


    choiceBotNum = random.randint(1,3)
    if(choiceBotNum == 1):
        choiceBot = "Rock"
    elif(choiceBotNum == 2):
        choiceBot = "Paper"
    elif(choiceBotNum == 3):
       choiceBot= "Scissors"
    else:
      print("Error occured with bot")
    if(choiceUser == "rock"):
     choiceUserNum = 1
    elif(choiceUser == "paper"):
        choiceUserNum = 2
    elif(choiceUser == "scissors"):
        choiceUserNum = 3
    else:
        print("Invalid input")

    print(choiceUser)
    print(choiceBot)

    if(choiceUserNum == 1 and choiceBotNum == 2 or choiceUserNum == 2 and choiceBotNum == 3 or choiceUserNum == 3 and choiceBotNum == 1):
      print("The bot won")
      botScore += 1
    elif(choiceUserNum == choiceBotNum):
      print("Its a draw!")
    else:
     print("You won")
     userScore += 1

    if(botScore == 3):
       winner = True
       print("You won the battle but the bot won the war")
    elif(userScore == 3):
       winner = True
       print("You won the battle and the war")
    else:
       print("You need {} to complete the game".format(3 - userScore))
       print("Bot needs {} to complete the game".format(3 - botScore))
print("Game over")