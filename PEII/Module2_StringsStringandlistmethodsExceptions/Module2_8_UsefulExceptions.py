def read_int(prompt, minim, maxim):
    try:
        x = int(input(prompt))
        assert minim <= x <= maxim
        return x
    except ValueError:
        print("Invalid input.")
    except AssertionError:
        print("The value is not within the specified range.")


v = read_int("Enter number from -10 to 10: ", -10, 10)

print("The number is", v)
