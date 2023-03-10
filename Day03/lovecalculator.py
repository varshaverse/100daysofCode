print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1 + name2

lower_case = combined.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

lovescore = int(str(true) + str(love))

print(lovescore)

if (lovescore < 10) or (lovescore > 90):
    print(f"your love score is {lovescore}, you go together like coke and mentos") 
elif(lovescore >= 40) and (lovescore <= 50):
    print(f"your score is {lovescore}, you are alright together")
else:
    print(f"your score is {lovescore}")







