# break & continue

#break
print("The loop terminates at 7:",end = "\n")

for n in range(1,10):
    if n == 7:
        break
    else:
        print(n)

# continue
print("The lopp only skips at 7 value:",end = "\n")

for m in range(1,10):
    if m == 7:
        continue
    else:
        print(m)

# printing 3 multiplication table by using continue
print("Printing 3 multiplication table by using continue")
for i in range(1,31):
    if i % 3 != 0:
        continue
    else:
        print(i)