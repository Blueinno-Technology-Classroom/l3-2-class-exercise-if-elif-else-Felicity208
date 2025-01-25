##################################################
'''
Q1: 
'''

weight = int(input("Enter your weight in kg:"))
height = int(input("Enter your height in cm:"))

bmi = weight / ((height/100) * (height/100))
if bmi >= 42:
    print(f'Your BMI is {bmi}, you are in obesity class III.')
elif bmi >= 35:
    print(f'Your BMI is {bmi}, you are in obesity class II.')
elif bmi >= 30:
    print(f'Your BMI is {bmi}, you are in obesity class I.')
elif bmi >= 25:
    print(f'Your BMI is {bmi}, you are overweight.')
elif bmi >= 18.5:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi <= 18.5:
    print(f'Your BMI is {bmi}, you are underweight')

# TODO: Write your code here

##################################################
'''
Q2:
'''

size = input("Size(S, M, L):")
pepperoni = input("Add pepperoni? (Y/N):")
cheese = input("Extra cheese? (Y/N):")
bill = 0
fun = 0

if size == "S":
    bill += 45
elif size == "M":
    bill += 50
elif size == "L":
    bill += 55
else:
    fun += 1
    bill += 60

if pepperoni == "Y":
    if size == "S":
        bill += 5
    elif size == "M" or size == "L":
        bill += 8

if cheese == "Y":
    bill += 3

print(f"Your final bill is ${bill}.")
if fun == 1:
    print("You got +$60 for messing around, Try again")


# TODO: Write your code here

##################################################
