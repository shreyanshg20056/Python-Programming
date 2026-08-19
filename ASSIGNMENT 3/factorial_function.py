fact = 1
def factorial(n,fact):

    for i in range(n,0,-1):
        fact = fact * i
    print(f"The Factorial Of {n} is: {fact} ")

num = int(input("Enter a number:"))
factorial(num,fact)