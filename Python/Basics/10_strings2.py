# Indexing is the method of slicing where we gave character index to print that character, But if we want to print several characters in the same line then we use slicing.
# slicing is a method of string where we print character from start to end at given step and its syntax is: string[start:end:step].
# The difference btw slicing and indexing is that if there any out of bounds or any error then slicing did not show it while indexing shows it.
course = "Python's course for beginners"
print(course)
print(course[-6])
print(course[::-1])
print(course[5:-3])
print(course[1:-1])
print(len(course))
# print(course[1:len(course)-5])
