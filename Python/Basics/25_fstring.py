# String Formatting In Python
# String formatting can be done in python using the format method
txt = "For Only {price:.2f} dollars!"
print(txt.format(price=49.09999))

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Shriyansh"
print(letter.format(country,name),"\n\n Or")


# f-string in python
# f-string simplify the print format by this method we can by apply curly brackets print variable and without it it simply print string otherwise.
print(f"\n Hey my name is {name} and I am from {country}")


