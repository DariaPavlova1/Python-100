# • Don't change the code below 4 print"Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# " Don't change the code above b
#Write your code below this line 4

compare_characters = "true love"
true = 0
love = 0
name = name1 + name2
times = name.lower().count(compare_characters[0])
true += times
times = name.lower().count(compare_characters[1])
true += times
times = name.lower().count(compare_characters[2])
true += times
times = name.lower().count(compare_characters[3])
true += times
times = name.lower().count(compare_characters[5])
love += times
times = name.lower().count(compare_characters[6])
love += times
times = name.lower().count(compare_characters[7])
love += times
times = name.lower().count(compare_characters[8])
love += times
love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

