# # arguments, keyword arguments, syntax, escape chars.

print("Hello, World!")

print('Hello, Python!')  # Single quotes works.

# print(Hello, Python!) # Without quotes syntax not valid.

# print"Hello,Python!" # Without parentheses SyntaxError.

# print("Hello") print("Bob") # Need separate lines or SyntaxError.

print(
    "Bobby!"
)               # This actually works. Multi-line Syntax as in
                # defining functions.

print("How about two lines")
print("of text.")

print("How about two lines of text")
print()  # This line is interpreted as a blank line or "newline".
print("with a space.")

# Escape characters and newline.
print("This is a string\nbroken by an escape character and newline.")

# To print \. Escape the escape character.
print("\\")
print("\"")

# Print with multiple arguments. Comma-separated. Auto-spaced with strings.
print("Once upon", "a", "time.")

# Positional argumentation. Arg meaning determined by order.
print("1st argument", "is followed", "by 2nd.")

# Keyword argumentation. Arg meaning determined by keyword identifier.
# IMPORTANT: Kwargs have to come after posargs.
# Here using "end="
print("The keyword", "determines ", end="last word.")
print("Default value", "for last keyword", "is newline.", end=" ")
print("Not with this.")

# Kwarg of "sep=". Determines separator.
print("I", "would", "like", "to", "combine", "these.", sep="-")
print("I", "would", "like", "to", "combine", "these.", sep="")
print("I", "would", "like", "to", "combine", "these.", sep="\n")

# Experiments with strings.
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Same as:
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# Double, line-broken:
print("    *\n   * *\n  *   *\n *     *\n***"
      "   ***\n  *   *\n  *   *\n  *****\n"*2)

# Side-by-side:
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

