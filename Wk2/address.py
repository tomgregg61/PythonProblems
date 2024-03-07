surname = (input("Please enter surname: "))
houseNo = int(input("Please enter house number: "))
roadName = input("PLease enter road name: ")
townName = input("Please enter town name: ")
print("""Mr and Mrs {surname},
{houseNo}, {roadName}
{townName}""".format(surname = surname,houseNo = houseNo,roadName = roadName,townName = townName))
