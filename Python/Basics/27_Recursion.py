# Recursion
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python,weknow that a function can call other functions.It is evenly possible for the functtion to call itself.That types of construct are termed as recursive function.
# Example:

def factorial(n):
  if(n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))
print(factorial(6))
print(factorial(7))


