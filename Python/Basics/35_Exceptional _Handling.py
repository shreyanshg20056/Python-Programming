# Raising Custom Errors
# In Python,we can raise custom errors by using the raise keyword.
# In Previous Tutorial,We learned about different built-in exceptions in python and 
# why it is important to handle exceptions.However,
# Sometimes we may need to create our own custom exceptions that serve our purpose.

a = int(input("Enter Value: "))

if(a<5 or a>9):
  raise ValueError("Value Should Be Between 5 and 9")
