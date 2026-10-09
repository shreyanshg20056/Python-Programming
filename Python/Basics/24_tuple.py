# Tuples Are Nonchangeable/Immutable.
# If you want to change items of tuples then you can indirectly convert tuple into list and then change it and then convert into tuple but we cannot directly change tuple.
# Example:
countries = ("Spain","India","USA","Germany","Iceland")
temp = list(countries)
temp.append("Greenland")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
# print(countries)


t = (1,4,3,21,3,5,1,6,32,2)
res = t.count(1)
print("Count of 1 in t is:",res)
print(t.index(2))
print(t.index(1,1,7))#by this we can find first occurence between indexes.
print(len(t))