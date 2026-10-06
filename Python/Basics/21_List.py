# Python List
# List are ordered collection of data items.
# They store multiple items in a single variable.
# List items are seperated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# Ex:
marks = [12,8,9,'hello',98.00]
print(marks)
# List Indexing is a method in which we can access items of list
# Accessing List Items can be done through putting index in square bracket for ex:list_name[index]
# Positive Indexing is the indexing which starts from 0 and ends at n-1 where n is length of items.
# Negative Indexing is the indexing which starts from -1 and ends at -n where n is length of items.
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(type(marks))

# If we want to check whether an item present in the list then:
# We can apply this for string also. 
if 9 in marks:
  print("9 is present")
else:
  print("9 is not present")

# List Slicing
# It access list through slicing method in which we can access by giving its starting point and ending point and if its out of range then it didnt give any errors. 
print(marks[-1::-1])
print(marks[:])
n = int(input())
lst = [i for i in range(4)]
lst1 = [i**2 for i in range(n) if i % 2 == 0]
print(lst)
print(lst1)
