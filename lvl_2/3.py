# CHALLENGE 1: Write a function that takes in two integers and
#              multiplies them together then returns the result.
def multiplier(int1, int2):
  return int1 * int2

# CHALLENGE 2: Run the function from CHALLENGE 1, passing in the
#              integers 99 and 52 and print the result.
result = multiplier(99, 52)
print(result)

# CHALLENGE 3: Write a function that takes two integers and prints
#              the string "I am X ft Y inches tall", replacing the
#              X and Y with the numbers passed into the function.
def height(x, y):
  return ("I am %d ft %d inches tall" % (x, y))

# CHALLENGE 4: Run the function from CHALLENGE 3, passing in 6 and 2
#              as the parameters.
print(height(6, 2))
