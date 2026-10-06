# Operators performs operations btw two operands.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
opt = input("Enter Operator:")

if opt == '+':
  print(a + b)
elif opt == '-':
  print(a - b)
elif opt == '*':
  print(a * b)
elif opt == '/':
  print(a / b)
elif opt == '%':
  print(a % b)
elif opt == '//':
  print(a // b)
else:
  print("Operator not available!!")