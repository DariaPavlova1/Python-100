import random

participants=input("Pleae give me names of all participants separated by space ' '")
participants_list = participants.split(" ")

winner_index = random.randint(0, len(participants_list - 1))
winner = participants_list[winner_index]
print(f"{winner}, you're paying today!")

