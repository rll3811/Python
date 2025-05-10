# Task: 01

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
f = factorial(n)
print("Factorial of ", n, " is:", f)

# Task: 02

import math

def maths(n):
    if n>0:
        sqrt = round(math.sqrt(n),4)
        log = round(math.log(n),4)
        sin = round(math.sin(n),4)
    else:
        sqrt = log = sin = "Invalid number."
    return sqrt, log, sin

n = float(input("Enter a number: "))
sqrt, log, sin = maths(n)
print("Square root of", n, "is:", sqrt)
print("Natural logarithm of", n, "is:", log)
print("Sine of", n, "is:", sin)

########################################################################

########

########################################################################

# Task: 01

def factorial(n):                                    # Defining the function.
    fact = 1
    for i in range(1,n+1):
        fact *= i                                    # Updating the factorial by multiplying each number up to n.
    return fact                                      # Return the factorial.

n = int(input("Enter a number: "))                   # Input value of the number to the function.
f = factorial(n)                                     # Calling the function and storeing the returning values.
print("Factorial of ", n, " is:", f)

# Task: 02

import math                                          # Importing the math library.

def maths(n):                                        # Defining the function.
    if n>0:                                          # Checking positive n.
        sqrt = round(math.sqrt(n),4)                 # Calculating the square root.
        log = round(math.log(n),4)                   # Calculating the log.
        sin = round(math.sin(n),4)                   # Calculating the sine.
    else:
        sqrt = log = sin = "Invalid number."
    return sqrt, log, sin                            # Returning the required values.

n = float(input("Enter a number: "))                 # Input number to the function.
sqrt, log, sin = maths(n)                            # Calling the function and storeing the returning values.
print("Square root of", n, "is:", sqrt)
print("Natural logarithm of", n, "is:", log)
print("Sine of", n, "is:", sin)
