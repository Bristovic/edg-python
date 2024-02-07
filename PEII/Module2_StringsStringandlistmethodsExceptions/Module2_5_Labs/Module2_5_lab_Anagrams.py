# program to check if strings are anagrams of one another
def anagram_check():
    to_check = input("""Enter strings, separated by #,
     to check if they are anagrams: """).lower().replace(" ", "")

    anags = to_check.split("#")

    if len(anags) <= 1:
        print("Too few strings entered. Check separator.")
        return

    else:
        new_anags = []
        for el in anags:
            new_el = []
            for ch in el:
                new_el.append(ord(ch))
            new_anags.append(sorted(new_el))

        anag_state = "are"

        for i in range(len(new_anags)-1):
            if new_anags[i] == new_anags[i + 1]:
                continue
            else:
                anag_state = "are not"

        print("The entered strings", anag_state, "anagrams.")


anagram_check()
