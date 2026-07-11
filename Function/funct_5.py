# types of arguments
#Positional Arguments - passing the arguments in order of their positions

def add1(n1,n2):
    return n1 + n2

result = add1(2,5)
print(f"This is the result of Positional argument: {result}")

# Default argument
# The non-default var always come before default ones
def add2(n1,n2=4):
    return n1 + n2

result2 = add2(6,5)
print(f"This is the result of Default argument: {result2}")

# Keyword Argument
# In Keyword Argument, we give the value of variable direct from calling the function
result = add2(n1=50, n2=10)
print(result)
