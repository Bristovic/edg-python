# simple 2-parameter function for bmi
def bmi_func(weight, height):
    return weight/height ** 2


# test data
print(bmi_func(52.5, 1.65))


# updated 2-parameter function checking for reliable inputs
def bmi_func_2(weight, height):
    if (height < 1.0 or height > 2.5
            or weight < 20 or weight > 200):
        return None
    return weight / height ** 2


# test data for suspicious inputs
print(bmi_func_2(352.5, 1.65))


# convert lb to kg
def lb_to_kg(lb):
    return lb * 0.45359237


# check
lb_to_kg(1)


# convert feet and inches to metre
def ft_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


# test
print(ft_inch_to_m(6, 0))
print(ft_inch_to_m(6))


# combining code
print(bmi_func_2(weight=lb_to_kg(176),
                 height=ft_inch_to_m(5, 7)))


# checking if 3 lengths can be a triangle
# sum of 2 sides have to be longer than remaining side
def check_if_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True


# Check
print(check_if_triangle(1, 1, 1))
print(check_if_triangle(1, 1, 3))


# compact version
def check_if_triangle(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True


# Check
print(check_if_triangle(1, 1, 1))
print(check_if_triangle(1, 1, 3))


# even more compact
def check_if_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


# integrating it into a larger program
# enter in values
a = float(input("Enter length of the first side of the triangle."))
b = float(input("Enter length of the second side of the triangle."))
c = float(input("Enter length of the third side of the triangle."))

# check if they are legitimate for a triangle
if check_if_triangle(a, b, c):
    print("Yes, it can be a triangle.")
else:
    print("No, it can't be a triangle.")


# check if right angle triangle with pythagoras theorem
def right_angle_triangle(a, b, c):
    if not check_if_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2


print(right_angle_triangle(5, 3, 4))
print(right_angle_triangle(1, 3, 4))


# function to evaluate triangle area with Heron's formula
def heron_formula(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


# function to check if triangle and if yes return area
def triangle_area(a, b, c):
    if not check_if_triangle(a, b, c):
        return None
    return heron_formula(a, b, c)


# test returns not exactly 0.5 (due to nature of floats)
print(triangle_area(1.0, 1.0, (2.0 ** 0.5)))


# factorial function
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


# test data
for n in range(1, 6):  # testing
    print(n, factorial_function(n))


# fibonacci numbers
def fib_num(n):
    if n < 1:
        return None
    fib = 1
    if n < 3:
        return fib
    else:
        fib_1st = 1
        fib_2nd = 1
        for i in range(3, n + 1):
            fib = fib_1st + fib_2nd
            fib_1st, fib_2nd = fib_2nd, fib
        return fib


# recursion
# use recursion to shorten code
def fib_num_2(n):
    if n < 1:
        return None
    fib = 1
    if n < 3:
        return fib
    return fib_num_2(n - 1) + fib_num_2(n - 2)


# test data
for n in range(1, 10):  # testing
    print(n, "->", fib_num_2(n))


# reducing factorial code
def factorial_2(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_2(n - 1)


factorial_2(5)
