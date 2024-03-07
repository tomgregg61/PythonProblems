heightFeet = int(input("Please enter your height in feet and inches starting with feet: "))
heightInches = int(input("Please enter your height in inches: "))

totalInches = (heightFeet * 12) + heightInches
heightCm = totalInches * 2.54
heightMm = heightCm * 10
heightM = heightCm / 100
heightKm = heightM / 1000

print("Height in kilometres:", heightKm)
print("Height in metres:", heightM)
print("Height in centimetres:", heightCm)
print("height in millimetres:", heightMm)