arr = []
for i in range(5):
    arr += [int(input("Enter an integer value: "))]

print(arr)

for i in range(len(arr)):
    value = arr[i]
    j = i - 1
    while (j >= 0 and arr[j] > value):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = value

print(arr)
