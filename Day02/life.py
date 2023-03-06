age = input("What is your current age? ")

ageint= int(age)

yearsremaining = 90 - ageint
daysremaining = yearsremaining *365
weeksremaining = yearsremaining * 52
monthsremaining = yearsremaining * 12

print(f"You have {daysremaining} days, {weeksremaining} weeks, and {weeksremaining} months left.")