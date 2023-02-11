print("Welcome to Tresure Island. Your mission is to find the treasure.")
# choice=input("Would you like to go left or right?").lower()
# if choice == "right":
#     print("Game Over.")
# elif choice == "left":
#     choice=input("Would you like to swim or wait?").lower()
#     if choice == "swim":
#         print("Game Over.")
#     elif choice == "wait":
#         choice=input("Which door you would like to open: red, blue or yellow?").lower()
#         if choice == "blue" or choice == "blues":
#             print("Game Over.")
#         else:
#             print("Your win!")

choice=input("Would you like to go left or right?").lower()
if choice == "left":
    choice=input("Would you like to swim or wait?").lower()
    if choice == "wait":
        choice=input("Which door you would like to open: red, blue or yellow?").lower()
        if choice == "yellow":
            print("Your win!")
        else:
            print("Game Over.") 
    else:
        print("Game Over.")   
else:
    print("Game Over.")  

