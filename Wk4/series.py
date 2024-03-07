negCount = 0
posCount = 0
for i in range(5):
    num = int(input("Please enter a number: " ))
    if(num < 0):
        negCount += num
    else:
        posCount += num
print("Sum of positive integers:", posCount)
print("Sum of negative integers:", negCount)