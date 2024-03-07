adult = 10.50
child = 7.30
concession = 8.40
runningTotal = 0

children = int(input("Please enter number of children: "))
adults = int(input("Please enter number of adults under 65: "))
adultsToPay = adults - (children // 10)
concessions = int(input("Please enter number of adults over age of 65: "))
collection = input("Will tickets be collected in person or delivered [delivered / pickup]: ")
if(collection == "delviered"):
    runningTotal += 2.34

runningTotal += (child * children) + max(0,(adultsToPay * adult)) + (concession * concessions)
if(runningTotal > 100):
    runningTotal *= 0.9

if(collection == "delivered"):
    runningTotal += 2.34

print ("Total bill is £{:.2f}".format(runningTotal))
