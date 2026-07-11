# Functions
# User-defined functions
def add(n1,n2):
    if n1 > n2:
        print(f"{n1} is greater than {n2}")
    else:
        print(f"{n1} is less than {n2}")

a = int(input())
b = int(input())
add(a,b)