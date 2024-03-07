months = {"January": 1, "February": 1, "March": 1, "April": 1, "May": 1, "June": 1, "July": 1, "August": 1, "September": 1, "October": 1, "November": 1, "December": 1}
for month in months:
    thisData = int(input("Please enter rainfall for {} ".format(month)))
    months[month] = thisData

highestFall = 0
for month in months:
    if months[month] > highestFall:
        highestFall = months[month]

rows, cols = (highestFall, 12)
arr = [["   " for i in range(cols)] for j in range(rows)]

currentMonth = 0
for month in months:
    for i in range(highestFall - months[month], highestFall):
        arr[i][currentMonth] = " x "
    currentMonth += 1

for rows in arr:
   for cols in rows:
      print(cols,end = " ")
   print()
print("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")