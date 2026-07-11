# membership operator = in & not in
# concatenation and repetition can not be done with sets
# Set are unordered and non-sequential - when we print set then its order changes from its declared positions
# Sets are Mutuable
# add() - When any element added then its randomly added as indexing sets cannot use
# remove() - it removes element by putting element into index
# discard() - it same works as remove() but if value is not present then it gives no error but remove() give key(value) error
num_1 = {1,3,5,7,9}
print(1 in num_1)
print(1 not in num_1)
num_1.add(5)
num_1.remove(1)
num_1.discard(5)
num_1.discard(100)
print(num_1)
