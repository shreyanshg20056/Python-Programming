# range function - built-in function which is used to generate sequence of integers in a given int
# range(start,stop,step)
#
# for n in range(1,21,1):
#     print(n)
# for n in range(20,0,-1):
#     print(n)

profits = [9,11,6,10]

for index in range(len(profits)):
    q = index + 1
    print(f"Profit for quarter {q} is {profits[index]}")