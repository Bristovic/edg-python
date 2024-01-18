# the `input()` function
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# input() can include prompt in argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# Can't include operators. This won't work.

# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Type-casting to convert string input to float
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Assignment modifying pythag code.
side_a = float(input("What is the length of side a? "))
side_b = float(input("What is the length of side b? "))
print("The length of c (the hypotenuse) is: ",
      ((side_a ** 2) + (side_b ** 2)) ** 0.5
      )

# String operators + and *.
x = "Ab"
y = "ba"
print("The band is: ", x + y)

x = "ga"
print("A rude term for dementia is 'going", x * 2 + "'.")

# Draws a rectangle
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Convert number to string
print(str("1"))

# Assignment: mathematical operations
# input a float value for variable a here
num_a = float(input("Enter the first number: "))
# input a float value for variable b here
num_b = float(input("Enter the second number: "))

# output the result of addition here
print("Adding these two produces: " + str(num_a + num_b))
# output the result of subtraction here
print("Subtracting the first from the second produces: "
      + str(num_a - num_b)
      )
# output the result of multiplication here
print("Multiplying the two produces: " + str(num_a * num_b))
# output the result of division here
print("Dividing the first by the second produces: "
      + str(num_a / num_b)
      )

print("\nThat's all, folks!")

# Second test assignment
x = float(input("Enter value for x: "))
y = (1 / (x + (1 / (x + (1 / (x + (1 / x)))))))
print("y =", y)

# Third test assignment: end time calculation
# ASSIGNMENT
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

time = (hour * 60) + mins  # Convert time to minutes
dura_time = time + dura  # Time in minutes at event end.

# Event end in minutes and hours and ensure within 24
end_time = str(((dura_time // 60) % 24)) + ":" + str((dura_time % 60))
print("The event will end at: " + end_time)

# Checking type
x = input("Enter a number: ")
print(type(x))

x = 1
y = 2
z = x
x = y
y = z
print(x, y)
