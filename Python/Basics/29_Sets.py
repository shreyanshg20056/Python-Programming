s0 = {1,2,3,4,5,6,7,8,9,10}
# Joining Sets
# Sets in Python more or less work in 
# the same way as sets in mathematics.
# We can perform operations like union and 
# intersection on the sets just like in mathematics.

# 1. union() and update()
# Union and Update methods prints all items that are present in the two sets.
# The union method return a new set whereas update method adds items into the existing set from another set.
# Example:

s1 = {1,4,2,7,3}
s2 = {4,7,2,72,5,6}
s3 = s1.union(s2)
# print(s3)
# s1.update(s2)
# print(s1)

# 2. intersection() and intersection_update()
# Its same as above intersection takes common numbers from both sets and store in an another set whereas intersection_update() does the same work but it store into existing set.

s4 = s1.intersection(s2)
s2.intersection_update(s3)
# print(s4)
# print(s2)

# 3. symmetric_difference( ) and symmetric_difference_update( )
# In this symmetric difference method results in another set those items which not in neither set which means uncommon items.
# In second one it do the same work but stored in existing set.

s6 = {5,8,5,0}
s7 = {1,3,2,6}
# s8 = s6.symmetric_difference(s7)
# print(s8)
# s6.symmetric_difference_update(s7)
# print(s6)

# 4. difference() and difference_update()
# In the difference(),It removes another set items from the original set and stored in another set whereas in difference_update() it store in existing original set

# s9 = s6.difference(s7)
# print(s9)
# s6.difference_update(s7)
# print(s6)

# Set Methods
# isdisjoint(): The isdisjoint() method checks 
# if items of given set are present in another 
# set.This method returns false if items are present,
# else it return true.
print(s6.isdisjoint(s7))

# issuperset(): The issuperset() method checks 
# when a set have all elements of second set 
# then it returns true else false.

print(s0.issuperset(s7))
print(s0.issuperset(s6))

# issubset():
# The issubset() method is if any set having 
# all elements that are present in 
# another set then it return true else false.

print(s7.issubset(s0))

# .add(item):If you want to add an item to a set then use add() method.
s7.add(4)
print(s7)

# .update():If we want to add more than one item or iterable object then we use update() method.
s7.update(s2)
print(s7)

# .remove()
s6.remove(0)#it shows error.
print(s6)
# .discard()
s7.discard(1)#it don't.
print(s7)

# .pop():It removes last element of the set but we dont know which element is removed but we can store it and then find out which element is popped out.
a = s7.pop()
print(s7)
print(a)

# del : It is a keyword that can deletes entire set.
del s6
# print(s6)

# clear():This set deletes all elements and returns empty set.
s0.clear()
print(s0)