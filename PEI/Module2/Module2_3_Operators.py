# Python as a calculator.
print(2+2)

# Arithmetic operators
print(2 ** 3)  # Exponentiation
print(2.0 ** 3)  # Exponentiation with floats.

print(2 * 3)  # Multiplication
print(2 * 3.)  # Multiplication with floats.

print(6 / 3)  # Division. Result always a float.
print(6.0 / 3)  # Division. Result always a float.

# Integer division
print(6 // 3)  # Integer division.
print(6 // 3.0)  # Integer division with float.

print(6 // 4)  # Integer division rounds to lesser whole number: 1
print(6.0 // 4.0)  # ALSO ROUNDS TO NEAREST LESSER WHOLE: 1.0

print(6 // -4)  # Rounds to -2 (as lower).
print(6 // -4.0)

# Remainder(modulo)
print(14 % 4)  # Gives remainder (2) after integer division.
# 14/4 is 3.5
# 14 // 4 is 3
# 0.5 * 4 is 2

# Addition and subtraction
print(4 + 2)  # Straightforward addition

print(4 - 4)  # Subtraction (binary)
print(-4 + 2)  # Changing sign (unary)
print(-4.0 - -2)  # Both. And float rule applies.

print(+2)  # Unary +. Rarely needed.

# Operator priorities and bindings
print(2 + 3 * 5)  # Hierarchy of priorities is after priority.

print(3 / 3 / 2)  # Equal priority follows binding (L to R, usually)
print(2 / 3 / 3)

# EXCEPTION: Exponentiation follows R to L binding.
print(2 ** 2 ** 3)  # 256 (2 ** 8) not 64 (4 ** 3)
print(2 ** 3 ** 2)

# Can always use brackets for clarity.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  # 10.0

print(-2 ** 3)

# Examples
print((2 ** 4), (2 * 4.), (2 * 4))  # 16, 8.0, 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))  # -0.5, 0.5, 0, -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2))  # 2, -2, 512 
