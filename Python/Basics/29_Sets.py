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

s6 = {2,5,2,8,5,0}
s7 = {1,3,2,5,6}
s8 = s6.symmetric_difference(s7)
# print(s8)
# s6.symmetric_difference_update(s7)
# print(s6)

# 4. difference() and difference_update()
# In the difference(),It removes another set items from the original set and stored in another set whereas in difference_update() it store in existing original set

s9 = s6.difference(s7)
print(s9)
s6.difference_update(s7)
print(s6)