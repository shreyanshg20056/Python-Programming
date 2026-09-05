# Errors in Exceptional Handling
# Compile time error => syntax error & Indentation error
# age = 24
# print(age [Compile Error]
# age = 24
# if age >= 18:
# print(age) [Indentation Error]

# Exceptions => errors during execution
# print(10/0)
# x = 100
# print(x + y)

# How to handle exceptions? => try-except block

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

try:
  result = num1/num2
  print(result)
except ZeroDivisionError:
  print("The Denominator cannot be zero")
except ValueError:
  print("Inputs should be only be in digits")