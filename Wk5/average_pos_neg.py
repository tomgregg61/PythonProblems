negCount = 0
noOfPos = 0
posCount = 0
noOfNeg = 0
for i in range(10):
    num = int(input("Please enter a number: " ))
    if(num < 0):
        negCount += num
        noOfNeg += 1
    else:
        posCount += num
        noOfPos += 1
if(negCount == 0):
    noOfNeg += 1
if(posCount == 0):
    noOfPos += 1
print("Sum of positive integers:", posCount)
print("Sum of negative integers:", negCount)
print("Average of positive numbers:", (posCount / noOfPos))
print("Average of negative numbers:", (negCount / noOfNeg))
print()