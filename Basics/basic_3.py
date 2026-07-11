P = int(input("Enter Principal value:"))
R = int(input("Enter Rate value:"))
T = int(input("Enter Time value:"))
amount1 = P * (1 + R/100) ** T
amount2 = P * pow((1 + R/100), T)
print(amount1)
print(amount2)
