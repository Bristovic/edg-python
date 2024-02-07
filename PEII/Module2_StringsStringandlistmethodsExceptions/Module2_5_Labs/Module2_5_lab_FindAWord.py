# program to find if the chars of a string are hidden in a 2nd string
def word_find():
    to_find = (input("Enter the word whose characters to find: ")
               .lower().replace(" ", ""))
    to_search = (input("Enter the string to search: ")
                 .lower().replace(" ", ""))

    # one: searches to find what characters are in the string
    found_chars = []
    found = True

    for char in to_find:
        if to_search.find(char) != -1:
            found_chars.append(char)
        else:
            found = False

    if found:
        print("The characters of the word were all found.",
              "They were found in the following order: ",
              found_chars)
    elif not found_chars:
        print("No characters were found.")
    else:
        print("Not all characters were found."
              "The following were:",
              found_chars)


word_find()
