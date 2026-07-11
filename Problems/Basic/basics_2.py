A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
C = int(input("Enter C value:"))

if A>B & A>C:
    print(f"{A} is the largest number")
elif B>A & B>C:
    print(f"{B} is the largest number")
else:
    print(f"{C} is the largest number")
    