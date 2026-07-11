# break & continue
#break
# for n in range(1,10):
#     if n == 7:
#         break
#     else:
#         print(n)

# continue
# for n in range(1,10):
#     if n == 7:
#         continue
#     else:
#         print(n)
# printing 3 multiplication table by using continue
for n in range(1,31):
    if n % 3 != 0:
        continue
    else:
        print(n)