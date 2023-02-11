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

user_choice = input("Pleae choose rock,paper or scissors:1, 2 or 3")

random_number = random.randint(1,3)
if user_choice == 1:
    user_choice = rock
elif user_choice == 2:
    user_choice = paper
else:
    user_choice = scissors
print(f"Your choice is {user_choice}")

if random_number == 1:
    computer_choice = rock
elif random_number == 2:
    computer_choice = paper
else:
    computer_choice = scissors
print(f"Computer choice is {computer_choice}")



if (computer_choice == rock and user_choice == scissors) or (computer_choice == scissors and user_choice == rock) or (computer_choice == scissors and user_choice == rock):
    print("You lost.")
elif (user_choice == rock and computer_choice == scissors) or (user_choice == scissors and computer_choice == rock) or (user_choice == scissors and computer_choice == rock):
    print("You won.")
else:
    print("It's a draw")



