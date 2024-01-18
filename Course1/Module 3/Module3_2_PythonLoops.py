# while loops
x = 3
while x > 0:
    print(x)
    x = x-1

# while to find largest number
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
# Print the largest number.
print("The largest number is:", largest_number)

# Another example
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
odd_numbers = 0
even_numbers = 0
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Assignment. Number guessing.
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("Enter your guess here:"))
while guess != 777:
    print("Haha! You are stuck in my loop!")
    guess = int(input("Guess again:"))
print("Well done, muggle! You are free now.")

# Looping with for
for i in range(100):
    print("i is now", i)

# Looping with for with 3 arguments (start, finish, steps)
for i in range(2, 8, 3):
    print("The value of i is currently", i)

# Looping for expo
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# Assignment: Mississippi
import time

for sec in range(1, 6):
    print(sec, "Mississippi.")
    time.sleep(1)
print("Ready or not, here I come.")

# break and continue
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# breaking a loop with break
largest_number = -99999999
counter = 0
while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# Assignment: Chupacabra break
while True:
    word = str(input("Enter a word:"))
    if word == "chupacabra":
        break
print("You've successfully left the loop")

# Assignment: Vowel Eater continue
user_word = input("Enter a word. Watch it be devoured.")
user_word = user_word.upper()

for letter in user_word:
    if (letter == "A" or letter == "E" or letter == "I"
            or letter == "O" or letter == "U"):
        continue
    else:
        print(letter)

# Assignment: Vowel Eater upgraded
user_word = input("Enter a word. Watch it be devoured.").upper()
no_vowels_word = ""
for letter in user_word:
    if (letter == "A" or letter == "E" or letter == "I"
            or letter == "O" or letter == "U"):
        continue
    else:
        no_vowels_word += letter
print(no_vowels_word)

# else also exists in while loops. always executes after loop.
i = 6
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# for else
i = 111
for i in range(0):
    print(i)
else:
    print("else:", i)

# Assignment: Block pyramid
block_no = int(input("How many blocks do you have?"))
height = 0
layer_width = 0
while True:
    # Check that building a layer won't mean negative blocks.
    if block_no - (layer_width+1) < 0:
        break
    # Add to height, increase layer width, sub width from number.
    else:
        height += 1
        layer_width += 1
        block_no -= layer_width
print(f"The tower can be {height} layers tall.")

# Assignment: Lothar Collatz hypothesis
c0 = 0
steps = 0
while c0 <= 0:
    c0 = int(input("Enter a natural (non-negative, non-zero integer):"))
while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 /= 2
        print(f"c0 divided by 2 is {int(c0)}.")
    else:
        c0 = (c0 * 3) + 1
        print(f"c0 times 3 plus 1 is {int(c0)}.")
print(f"c0 is now equal to 1. It took {steps} steps."
      f" Lothar Collatz approves!")

# Exercise: extracting names
email = "alberticus.von.pimplestein@argblast.com"
name = ""
for ch in email:
    if ch == "@":
        break
    else:
        name += ch
print(name)

# Exercise: replacing x
number = ""
for digit in "0165031806510":
    if digit == "0":
        number += "x"
    else:
        number += digit
print(number)


