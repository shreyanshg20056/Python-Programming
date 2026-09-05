try:
 with open("python12","rt") as fh:
  data = fh.read()
  print(data)
except FileNotFoundError as file_err:
 print("File does not exists.")
 print(file_err)
else:
 print("else Block") 
 print(data)
finally:
 print("Finally Block") 

print(" ")

try:
 with open("python15","rt") as fh:
  data = fh.read()
  print(data)
except FileNotFoundError as file_err:
 print("File does not exists.")
 print(file_err)
else:
 print(data)
 