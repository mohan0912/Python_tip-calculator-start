#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

totalBill = input("what was the total bill? $")
tipPercentage = input("what percentage tip would you like to give? 10, 12. or 15? ")
numberPerson = input("How many people to split the bill? ")


tipCalculated = round((float(totalBill)/int(numberPerson))+((float(tipPercentage) * float(totalBill))/100)/int(numberPerson),2)
print(f"Each person should pay: ${tipCalculated}")

