# equality operator
1 == 2  # False
1 == 1.0  # True, as Python recognises int-float comparison

# inequality operator
1 != 0  # True
1 != 1  # False

# greater than
1 > 2  # False
3 > 2  # True
2 > 2  # False

# greater than or equal to (non-strict)
1 >= 1 # True

# less than
1 < 2  #True
1 <= 2  # True

# Exercise
n = float(input("Enter a number: "))
print(n>=100)

# Shortened
print(float(input("Enter a number: "))>=100)

# if-else
n = float(input("Enter a number: "))
if n >= 100:
    print("Number is greater than or equal to 100.")
else:
    print("Number is less than 100.")

# nested if-else (cascade)
n = float(input("Enter a number: "))
if n >= 100:
    if n >= 200:
        print("Number is greater than 199.")
    else:
        print("The number is between 100 and 200.")
else:
    if n > 0:
        print("The number is positive, but less than 100.")
    else:
        print("The number is negative.")

# better with elif
n = float(input("Enter a number: "))    
if n >= 200:
    print("Number is greater than 199.")
elif n >= 100:
    print("The number is between 100 and 200.")
elif n > 0:
    print("The number is positive, but less than 100.")
else:
    print("The number is negative.")

# Assignment: Spathiphyllum
what_plant = input("Give me the plant: ")
if what_plant == "Spathiphyllum":
    print("Yes! Spathiphyllum is the best plant ever.")
elif what_plant == "spathiphyllum":
    print("No, I want big Spathiphyllum.")
else:
    print("Spathiphyllum! Not", what_plant)

# Assignment: tax
tax = 0
income = float(input("Enter your income in digits:"))
if income <= 85_528:
    tax = ((0.18*income) - 556.02)
else:
    tax = (14_839.02 + (0.32 * (income-85_528)))

if tax <= 0:
    print("No tax for you, poor soul.")
else:
    print("Your tax amount is:", round(tax), "thalers.")

# Assignment: leap years
year = int(input("What year is it?"))
year_type = ""
if year < 1582:
    print("Year not within the Gregorian period.")
    exit()
elif year % 4 != 0:
    year_type = "common year"
elif year % 100 != 0:
    year_type = "leap year"
elif year % 400 != 0:
    year_type = "common year"
else:
    year_type = "leap year"
print("The selected year is a", year_type + ".")
exit()


