# Finally Clause
# The Finally Code Block is also part of exceptional handling.
# When we handle exception using the try and except block,
# we can include a finally block at the end.
# The finally block is always executed,so it is generally 
# used for doing the concluding tasks like closing file resources 
# or closing database connection or may be ending the program execution 
# with a delightful message.
try:
  n = int(input("Enter a number: "))
  print(f"The Multiplication Table of {n}:")
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
except ValueError:
  print("Invalid Input")
finally:# It simply means if code executed only till try yet it still execute same as always.
  print("I am always executed")
 