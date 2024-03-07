numOfMins = int(input("Please enter number of minutes to be billed: "))
callRate = 0.15
vatRate = 0.2
print("Number of minutes used:", numOfMins)
basicCharge = numOfMins * callRate
print("Basic call charge: £{:.2f}".format(basicCharge))
vatCharge = basicCharge * 0.2
print("VAT due: £{:.2f}".format(vatCharge))
totalBill = basicCharge + vatCharge
print("Total bill: £{:.2f}".format(totalBill))