# It's a user defined arithmetic function
def arithmetic(n1,n2):
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    return add, sub, mul, div

num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
res1, res2, res3, res4 = arithmetic(num1,num2)
print(f"The Addition of {num1} and {num2} is {res1}")
print(f"The Difference of {num1} and {num2} is {res2}")
print(f"The Multiplication of {num1} and {num2} is {res3}")
print(f"The Division of {num1} and {num2} is {res4}")