# Type casting is a method where we change type by functions like int(),float(),list(),tuple(),...,etc.
# There are two types of type casting
# implicit type cating is a automated type casting that python itself type casts by adding or any operation we've done.
# explicit type casting is a when user itself type casts data type into another data type by using functions.
# It Type Cast Based category of the data if it numeric then it cannot converted to strings through type casting.
a = "1"
b = "34"
print(a+b)
print(type(a+b))
result = int(a + b)
print(result)
print(type(result))
