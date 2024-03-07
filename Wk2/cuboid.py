width = int(input("enter width: "))
length = int(input("enter length: "))
height = int(input("enter height: "))

volume = width*length*height
surfaceArea = (width * length * 2) + (length * height * 2) + (width * height * 2)

print("Surface area =", surfaceArea)
print("Volume =", volume)