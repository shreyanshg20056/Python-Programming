# Exceptional Handling
# Exceptional Handling is the process of responding to unwanted or unexpected events when a program runs.
# Exceptional Handling deals with these events avoiding program  or system crashing.


try:
  n = int(input("Enter a number: "))
  print(f"The Multiplication Table of {n}:")
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
except ValueError:
  print("Invalid Input")