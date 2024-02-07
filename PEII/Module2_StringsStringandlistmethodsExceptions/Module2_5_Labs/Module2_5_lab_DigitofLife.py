# program to find "digit of life"
# i.e. some of all digits in birthdate until < 10


def life_digit():
    bdate = (input("Enter your birthday in YYYY-MM-DD format: ")
             .replace("-", ""))
    try:
        int(bdate)
    except ValueError:
        print("Please input digits only.")
    if len(bdate) != 8:
        print("Please input 8 digits only.")
        return
    else:
        bdate = list(bdate)
        b_num = sum([int(i) for i in bdate])

        while b_num > 9:
            b_num = sum([int(i) for i in str(b_num)])

    print(b_num)


life_digit()
