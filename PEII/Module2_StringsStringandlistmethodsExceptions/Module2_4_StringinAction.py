# Can use operators to compare chars. Will compare codepoints.
print("a" != "A")  # True
print("a" == "a")  # True

# With longer strings, compares codepoints one by one.
print("Alpha" == "Alpha")  # True
print("Alpha" != "alphA")  # True

# comparison determined by first char that is different
print("alpha" < "alphabet")  # True, as b codepoint > None
print("A" > "a")  # False because "A" codepoint lower no than "a"
print("dog" > "doc")  # True because g comes after c so higher no.

# strings of numbers are still just strings
print("10" != "010" != "10.0")

# can only compare number strings to numbers with "==" and "!="
# otherwise TypeError
print("10" == 10)  # False
print(10 != "10")  # True

# sorting
greek_letters = ["epsilon", "beta", "gamma", "alpha", "delta"]

# sorted function creates new list. original remains
greek_letters_sorted = sorted(greek_letters)
print(greek_letters_sorted)  # sorts alphabetically.
# NOTE: not the order of Greek letters themselves (would be if used symbols)

# sort method alters list in situ. alters original list
words_list = ["banana", "apple", "zebra", "elephant", "wombat"]
words_list.sort()
print(words_list)

# number to string conversion
x = str(12_300_123.452)

# reverse transform
y = float("123456.10")
z = int("12334")
print(y-z)


# 2.4 lab: LED display
# a needlessly complicated LED display function.
# could be further simplified by identifying commonalities and making
# branching trees. also removing redundant replacements.
def digit_construct():
    LED_on = "#"
    LED_num = list(input("Enter a number in digits: "))
    LED_display = []

    for LED_digit in LED_num:
        LED_matrix = [[" " for col in range(3)] for row in range(5)]
        if LED_digit == "1":
            for i in range(5):
                LED_matrix[i][2] = LED_on

        if LED_digit == "2":
            for i in range(0, 5, 2):
                for j in range(3):
                    LED_matrix[i][j] = LED_on
            LED_matrix[1][2] = LED_on
            LED_matrix[3][0] = LED_on

        if LED_digit == "3":
            for i in range(5):
                LED_matrix[i][2] = LED_on
            for i in range(0, 5, 2):
                LED_matrix[i][1] = LED_on
                LED_matrix[i][0] = LED_on

        if LED_digit == "4":
            for i in range(5):
                LED_matrix[i][2] = LED_on
            for i in range(3):
                LED_matrix[2][i] = LED_on
            LED_matrix[0][0] = LED_on
            LED_matrix[1][0] = LED_on

        if LED_digit == "5":
            for i in range(0, 5, 2):
                for j in range(3):
                    LED_matrix[i][j] = LED_on
            LED_matrix[1][0] = LED_on
            LED_matrix[3][2] = LED_on

        if LED_digit == "6":
            for i in range(5):
                LED_matrix[i][0] = LED_on
            for i in range(0, 6, 2):
                for j in range(3):
                    LED_matrix[i][j] = LED_on
            LED_matrix[3][2] = LED_on

        if LED_digit == "7":
            for i in range(5):
                LED_matrix[i][2] = LED_on
            for i in range(3):
                LED_matrix[0][i] = LED_on

        if LED_digit == "8":
            for row in range(5):
                for col in range(0, 4, 2):
                    LED_matrix[row][col] = LED_on
            for row in range(0, 6, 2):
                LED_matrix[row][1] = LED_on

        if LED_digit == "9":
            for row in range(5):
                LED_matrix[row][2] = LED_on
            for row in range(3):
                LED_matrix[row][0] = LED_on
            for row in range(0, 6, 2):
                for col in range(3):
                    LED_matrix[row][col] = LED_on

        for i in range(5):
            print(LED_matrix[i])
        print("\n")


digit_construct()
