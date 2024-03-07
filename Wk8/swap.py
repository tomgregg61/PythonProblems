entered = input("Enter two ints: ")
print("You've entered:", entered)
stringList = entered.split()
numList = [eval(i) for i in stringList]
def swap(nums):
    nums =[nums[1],nums[0]]
    return nums
swapped = swap(numList)
def print_int_list(intList = swapped):
    print("Your entries swapped: " + str(intList[0]) + " " + str(intList[1]))
print_int_list()