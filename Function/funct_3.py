# return keyword - this keyword is not printing the value, it's actually returns the value
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a value: "))

result = even_odd(num)
print(result)