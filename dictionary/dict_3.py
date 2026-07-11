# not allowed as key in dict - list, set,dict => mutable datatypes
# allowed as key in dict - str, int, float, bool, tuple => immutable datatypes
# keys of a dictionary can only be mutable datatypes!!
# Values can be any datatypes

student1 = {
    'id': 1001, 'name': 'John', 'marks': [89.5,75.1]
}
print(student1['marks'][1])
print(student1.keys(),type(student1.keys()))
print(student1.items(), type(student1.items()))
print(student1.values())
