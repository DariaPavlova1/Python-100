#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is you total bill?"))
tip = float(input("How much tip you would like to leave?"))
number_of_persons=float(input("How many people will be paying?"))
person_bill=((bill * tip / 100) + bill)/5
print(round(person_bill,2))