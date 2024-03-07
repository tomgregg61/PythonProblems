import math

areaToCover = (40 * 3.4 * 2) + (3.4 * 2 * 30)
cansNeeded = math.ceil(areaToCover / 5.1)
sizeOfCan = math.ceil(math.pi * 7.5 * 7.5 * 30)
cansPerBox = (60 * 30 * 35) // (sizeOfCan)
fullBoxesNeeded = math.floor(cansNeeded / cansPerBox)
CansNotInBox = math.ceil(cansNeeded - (fullBoxesNeeded * cansPerBox))

print("Numbers of cans required: {} \nNumber of cans in box: {} \nNumber of full boxes: {} \nCans not packed in boxes: {}".format(cansNeeded, cansPerBox, fullBoxesNeeded, CansNotInBox))