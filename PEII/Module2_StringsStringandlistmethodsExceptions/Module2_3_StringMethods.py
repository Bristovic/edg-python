# string methods
# capitalize() method
print("aBcD".capitalize())  # returns Abcd
print(" ALPHA".capitalize())  # "alpha" because first char is space
print("ALPHA".capitalize())
print("123".capitalize())  # no effect
print("γαβγδ".capitalize())

# center() method
print("ALPHA".center(10))
print("[" + "ALPHA".center(30) + "]")
print("[" + "CENTRED".center(25) + "]")

# center() with 2 paras
print("star centred".capitalize().center(25, "*"))

# endswith() method
print("epsilon".endswith("on"))
print("epsilon".endswith("off"))
print("zeta".endswith("A"))  # case sensitive

# find() method
print("Zeta".find("ta"))
print("Zeta".find("a"))
print("Zeta".find("lon"))  # -1 as non-existent substring

# find() method, 2-par
print("kappa".find("a", 2))

# using find() to search for all substring occurrences
wikipedia_text = """Wikipedia[note 3] is a free-content online encyclopedia, 
written and maintained by a community of volunteers, collectively known as 
Wikipedians, through open collaboration and the use of wiki-based editing 
system MediaWiki. Wikipedia is the largest and most-read reference work in 
history.[3][4] It consistently ranks as one of the 10 most popular websites 
in the world, and as of 2023 it is ranked the 6th most visited website on the 
Internet by Semrush.[5] Founded by Jimmy Wales and Larry Sanger, on January 
15, 2001, it is hosted by the Wikimedia Foundation, an American nonprofit 
organization that employed a staff of over 700 people by October 2023.[6] 
"""

fnd = wikipedia_text.find("it")
while fnd != -1:
    print(fnd)
    fnd = wikipedia_text.find("it", fnd + 1)

# 3-par permutation
print("banana".find("a"))
print("banana".find("a", 2))
print("banana".find("a", 4, 5))

# isalnum(). checks if all letter or digit. Bool return.
print("lambda30".isalnum())
print("is30%".isalnum())
print("lambda_30".isalnum())
print("isn't".isalnum())  # common
print("ΑβΓδ".isalnum())

# the isalpha() method. only letters
print("Beans".isalpha())
print("123ABC".isalpha())

# the isdigit() method. only numbers
print("123".isdigit())
print("123AD".isdigit())

# isspace(). only whitespaces (any kind)
# islower(). only lower
# isupper(). only upper

# the join() method
print(" ".join(["What", "is", "this"]))

# the lower() method
print("AAargGLe, WAaoOw SOO WEirRD!".lower().capitalize())

# lstrip() method with no par
print("[" + "   woah   ".lstrip() + "]")

# lstrip() method with one par
print("www.awebsite.com".lstrip("w."))
print("www.awebsite.com".lstrip(".com"))  # leading chars

# replace() method with two par
print("www.beansarebeansarebeans.com".replace("beans", "legumes"))
print("www.beansarebeansarebeans.com".replace("beans", ""))
print("www.beansarebeansarebeans.com".replace("", " "))

# replace() method with three par
print("www.beansarebeansarebeans.com".replace("beans", "legumes", 2))

# rfind() method. starts search from right
print("www.beansarebeansarebeans.com".rfind("beans", 0, 20))

# rstrip() method. lstrip but from right
print("www.beansarelegumes.com".rstrip(".com"))
print("{" + "   spaces   ".rstrip().lstrip() + "}")

# below strips all but either side. issue of takes all
print("www.wombatdoc.com".rstrip(".com").lstrip("www."))

# the split() method
print("Alpha     Beta\nDelta".split())

# startswith() method
print("omega".startswith("om"))
print("omega".startswith("ga"))

# strip() method
print("[" + "      spaces     ".strip() + "]")

# the swapcase() method
print("Upper, lOWER, miDDlE".swapcase())

# the title() method
print("thIS IS a MESSed up tiTLE".title())

# the upper() method
print("all Caps, bAAbaaaay!".upper())


# 2.3 exercise: Your own split
# my version has issues in that returns lots of empty strings
def my_split(strng):
    str_list = []
    word = ""
    for char in strng:
        if not char.isspace():
            word += char
        else:
            if word == "":
                continue
            else:
                str_list.append(word)
                word = ""
    if word != "":
        str_list.append(word)
    return str_list


# testdata
print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))
