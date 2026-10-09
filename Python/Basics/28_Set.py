# Python Sets
# Sets are unordered collection of items.
# They store multiple items in a single variable.
# Set items are separated by commas and enclosed in curly brackets {}.
# Sets are unchangable,meaning you cannot change items of the set once created.
# Sets do not contain duplicate items.
# Here we see that the item of set occur in random order and hence 
# they cannot be accessed using index numbers. 
# Example:

s = {1,4,7,4,9}
s1 = {} # If we use empty curly brackets for empty set then it shown as dictionary type.
s2 = set()#If we want to print empty set then we have to use set() constructor instead of {} empty curly brackets.
print(s,type(s))
print(s1,type(s1))
print(s2,type(s2))