# Caesar cipher example. simple roman cipher.
text = input("Enter message to encode: ")
cipher = ""
for char in text:
    if not char.isalpha():  # no digits. romans didn't use them.
        continue
    char = char.upper()  # only capitals (like Romans).
    code = ord(char) + 1  # moves ord to +1
    if code > ord("Z"):  # if this winds up greater than Z
        code = ord("A")  # will replace with A
    cipher += chr(code)  # add new char to cipher

print(cipher)


# Caesar cipher reverse
cipher = input("Enter your cipher: ")
text = ""
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord("A"):
        code = ord("Z")
    text += chr(code)

print(text)

# Number processor
line = input("Enter a line of numbers - separated by spaces: ")
strings = line.split()
total = 0
if strings == []:
    print("No number entered.")
else:
    try:
        for substr in strings:
            total += float(substr)
        print("The total is: ", total)
    except:
        print("Not a number.")

# iban validator
iban = input("Enter IBAN please: ")
iban = iban.replace(" ", "")

if not iban.isalnum():
    print("Invalid characters entered.")
elif len(iban) < 15:
    print("IBAN is too short.")
elif len(iban) > 31:
    print("IBAN is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ""
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord("A"))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN invalid.")


# lab: palindromes

