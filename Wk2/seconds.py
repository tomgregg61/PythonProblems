input = int(input("Please enter number of seconds: "))
hours = int(round(input / 60 / 60, 0))
left = input - (hours * 60 * 60)
minutes = int(round((left / 60), 0))
seconds = int(input - (minutes * 60) - (hours * 60 * 60))
print(hours)

print("{:<18}{:>8}{:>8}{:>8}".format("Input", "Hours", "Minutes", "Seconds"))
print("{:<18}{:>8}{:>8}{:>8}".format(input, hours, minutes, seconds))