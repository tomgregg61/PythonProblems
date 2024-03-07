
choice = input("Please enter an integer of at least 2 digits or -1 to quit: ")

nums = []
reverseNum = ""

while(len(choice) < 2 or len(choice) > 10):
    print("Invalid input please try again.")
    choice = input("Please enter an integer of at least 2 digits or -1 to quit: ")

if(len(choice) > 1 and len(choice) < 11 and choice != "-1"):
    for i in range(len(choice)):
        nums.append(choice[i])
    nums.reverse()
    for i in range(len(nums)):
        reverseNum += nums[i]
    print(reverseNum)
    print("Program end")
else:
    print("Program end")
