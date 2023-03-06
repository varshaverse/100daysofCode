print("welcome to the tip calculator")
finalbill = float((input("What was the total bill? ")))
tip = int(input("How much tip would you like to give? 10, 12, 15"))
people = int(input("How many people do you want to split the bill? "))

tippercent = tip/100
total_tip = finalbill * tippercent
finalbill = finalbill + total_tip
bill_perperson = finalbill /people

final_amount = round(bill_perperson,2)

print(f"Each person should pay: ${final_amount}")