# and, or, not

# bitwise operators: &, |, ~, ^

# bit shift
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# bitwise operation
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky! invert all bits and make leftmost into negative number,
        # then add 1 (ignoring overflow on first binary digit: so if
        # number is odd it won't change.
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)