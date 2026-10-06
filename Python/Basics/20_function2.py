# Functions Arguments and return statement
# There are four types of arguments that we can provide in a function:
# -> Default Arguments
# -> Keyword Arguments
# -> Variable Length Arguments
# -> Required Arguments

# Default Argument: We can provide a default value while creating a function.If a value is not provided in the function call for that argument it assumes a default value.
# Example:   
def average(a=5,b=9):
  return (a + b)/2


print("Average:",average(6,4))
print("Average:",average(6))
print("Average:",average(4))

# Keyword Argument
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.Hence,The order in which the arguments are passed does not matter.
# Example:

result = average(a=4,b=3)
print(result)

# Required Argument
# In case we dont pass the arguments with a key = value syntax,then it is necessary to pass the arguments in the correct positional order and the no. of arguments passed should match with actual function definition.
# Ex: When no. of arguments passed does not match to the actual function definition.
# if in function definition a value is not declared there then it means that become a required argument.

def add(a,b=7):
  return a+b
# a is required argument
print(add(a=4))

# Variable Length Argument
# Sometimes we may need to pass more arguments than those defined in the actual function.This can be done using Variable length arguments.

# There are Two Ways to achieve this:

# Arbitrary Arguments:
# While Creating a function,pass a * before the parameter name while defining the function.The function accesses the arguments by processing them in the form of tuple.
# Example:

def avg(*numbers): #it creates a tuple
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum += i
  print("Average is:",sum/len(numbers))

avg(5,6)

# Keyword Arbitrary Arguments:
# While creating a function,pass a* before the parameter name while defining the function.The function accesses the arguments by processing thhem in the form of directory.

def name(**name): #it creates dict
  print("Hello,", name["fname"],name["mname"],name["lname"])

  
print(name(mname ="Buchanan",lname= "Barnes",fname="James"))
# name(mname="Buchman",lname="Barnes")


# return statement goes back to the main function and return the value or any specific logic you returns.
def average(a=5,b=9):
  return (a + b)/2


print("Average:",average(6,4))


