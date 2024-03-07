nums = []
for i in range(0,5):
    number = int(input("Please enter number: "))
    nums.append(number)
reverseNums=[]
for i in range(len(nums) -1, -1, -1):
    reverseNums.append(nums[i])
print(nums)
print(reverseNums)