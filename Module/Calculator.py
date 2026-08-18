#This Is a simple user defined calculator module and in module 4,I am using it
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def square(a):
    return a ** 2

def modulus(a,b):
    return a % b

def sqrt(a):
    return a ** 0.5

#__name__ is a built-in variable in Python. It is used to check whether the module is being run directly or being imported into another module.
if __name__ == "__main__":
    a = 6
    b = 3
    result = mul(a, b)
    print(result)