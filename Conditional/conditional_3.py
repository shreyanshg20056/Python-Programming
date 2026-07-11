"""
if-elif-else statement
=>90, Grade A
<=89 & =>80, grade B
<=79 & =>70, grade C
<=69 & =>60, grade D
<=60, grade F
"""
total_marks = int(input("Enter the total marks:"))
if total_marks >=90:
    print("You've Secured Grade A")
elif total_marks <=89 & total_marks >=80:
    print("You've Secured Grade B")
elif total_marks <=79 & total_marks >=70:
    print("You've Secured Grade C")
elif total_marks <=69 & total_marks >=60:
    print("You've Secured Grade D")
else:
    print("You've Secured Grade F")