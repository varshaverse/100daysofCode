import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(images[computer_choice])

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
    print(images[choice])
else:
    print(images[choice])

if choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and choice == 2:
    print("You lose!")
elif computer_choice > choice:
    print("You lose")
elif choice > computer_choice:
    print("You win")
else:
  print("Tie")
