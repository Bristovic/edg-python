# 2.5 lab improving caesar cipher
def caesar_cipher_2():
    msg = input("Enter a message to encode: ")
    try:
        shift = int(input("Enter an encryption integer between 1 and 25: "))
        if shift > 25 or shift < 1:
            print("Not between 1 and 25")
            return
    except ValueError:
        print("Not an integer.")
        return

    encrypt = ""
    for sym in msg:
        if not sym.isalpha():
            encrypt += sym
            continue
        else:
            num = ord(sym) + shift
            if sym.isupper():
                if num > 90:
                    num = 64 + (num - 90)
            elif sym.islower():
                if num > 122:
                    num = 96 + (num - 122)
            encrypt += chr(num)
    print(encrypt)


caesar_cipher_2()
