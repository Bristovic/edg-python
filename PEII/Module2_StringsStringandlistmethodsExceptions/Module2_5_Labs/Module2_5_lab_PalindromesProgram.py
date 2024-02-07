# program to check if entered text is a palindrome
def palindrome_check_iter():
    to_check = list(input("Enter text to check if it is a palindrome: ")
                    .lower().replace(" ", ""))

    if not to_check:
        print("Not a palindrome")
        return
    elif to_check == list(reversed(to_check)):
        print("It is a palindrome!")
    else:
        print("Not a palindrome.")


palindrome_check_iter()
