# append():It adds given value in the end of the list.
# sort():It assembles list items in correct order in ascending or descending order.
# reverse():It reverses the list
# index(item):It gives first occurence of the given no.
# count():It counts given number in the list.
# copy():It creates a copy of the list that if you change the list then original list did not change.
# insert():It adds value in a specific index

lst = [1,2,34,5,52]
lst1 = [1,2,34,52,52]
lst.append(3)
# lst1.sort()
# lst.sort(reverse = True)
lst.reverse()
print(lst1.index(52))
print(lst1.count(52))
print(lst)
m = lst.copy()
m[0]=0
print(m)
# print(lst1)

lst1.insert(1,543)
print(lst1)

lst.extend(lst1)
print(lst)
k = lst + lst1
print(k)