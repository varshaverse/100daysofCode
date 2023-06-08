import random

names_string = input("Give me everyone's names, seperated by comma. ")

members = names_string.split(", ")

length_members = (len(members))

random_choice = random.randint(0,length_members-1)

person_pay = members[random_choice] #you can also use this without the function

#person_pay = random.choice(members) #you can use random.choice function
print(person_pay + " is going to buy the meal.")
