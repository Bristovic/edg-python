# Exceptions
# protecting from wrong data type
# trivial code
val = int(input("Enter a natural number: "))
print("The reciprocal of", val, "is", (1/val))

# simple code to check type of value
print(type(val) is int)

# but better way is try-except
try:
    val = int(input("Enter a natural number: "))
    print("The reciprocal of", val, "is", (1 / val))
except ValueError:  # when the data entered is wrong type
    print("Not a natural number.")
except ZeroDivisionError:  # when the nat number entered is 0
    print("Cannot divide by zero.")
except:  # when an error occurs not specified above, this runs
    print("Something unforeseen has happened. Sorry.")


