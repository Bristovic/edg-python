# Output looks the same.
print("2")
print(2)

# One is a string and the other an integer. Internal representation
# in computer is very different.

# Numeric literals. Underscores can be used as separators.
print(12_345_678)
print(12345678)

# Octal and hexadecimal (base-8 [0-6] and base-16 [0-15 using A-F for 10-15])
print(0o10)  # is equal to 8
print(0x4A)  # Is equal to 74

# Floats
print(0.4)
print(4.0)

# Integers
print(4)

# Floats with e (from exponent).
print(3e8)  # Speed of light.

# Planck's constant (h)
print(6.62607e-34)

# Python choosing other notation. Will display as 1e-32
print(0.00000000000000000000000000000001)

# Strings
print("I am a string.")
print("I need to use \"escape characters\" to display these quotes."
      " The escape character is \\.")
# OR
print('This way I don\'t need "escape characters" for the quote marks,'
      ' but I do for the apostrophe.')

# Booleans. True or False, 1 or 0.
print(True > False)
print(True < False)

# None. The NoneType lack of data.

print(None)
