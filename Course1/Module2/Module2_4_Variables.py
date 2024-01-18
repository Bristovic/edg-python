# Variable assignment through =
x = 1

# Simple maths problems. Pythagoras theorem.
a = 3.0
b = 4.0
c = ((a ** 2) + (b ** 2)) ** 0.5  # x ** 0.5 is same as square root.
print(c)

# Test assignment
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=",")

total_apples = john + mary + adam
print("Total number of apples: ", total_apples)

john, mary, adam = 2, 3, 4  # Multi-variable assignment.
print("Mary has", mary, "apples.")
print(f"John has {john} apples.")  # F-strings (learnt from DM)

# Assignment operator shortcuts
x = 2
x = x ** 2
print(x)
x = 2
x **= 2
print(x)

# Format is `var op= expression`

# Test assignment: miles to km, completing code.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Test assignment: 3x**3 - 2x**2 + 3x - 1
x = 2  # hardcode your test data here
x = float(x)

# write your code here
y = ((3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1)  # Need explicit *
print("y =", y)

# On comments
# Assignment to clarify comments (remove, exclude, change varname, etc)

# this program computes the number of seconds in a given number of hours
hours = 2  # number of hours
secs_per_hour = 3600  # number of seconds in 1 hour

print("Hours: ", hours)  # printing the number of hours
print("Seconds in Hours: ", hours * secs_per_hour)  # printing seconds in given hours

# Print "Goodbye"
print("Goodbye")

