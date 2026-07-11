a = int(input("Enter multiplication table number:"))
b = int(input("Enter second number for multiply:"))
for i in range(2,21,2):
    print(f"{a} * {b} = {i}")
    b = b + 1