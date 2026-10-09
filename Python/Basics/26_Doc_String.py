# Docstrings In Python
# Python Docstring are the string literals that appear right after the definition of a function,method,class,or module.
# Example:

def square(n):
  '''
  This Function Is Used To Find Square of a no.
  '''
  return n**2

x = int(input("enter no."))
print(square(x))
print(square.__doc__)

# Python Comments are desciption
# that help programmers better understand 
# the intent and functionality of the program.
# They are completely ignored by the Python Interpreter.

# Docstrings In Python
# Python Docstring are the string literals 
# that appear right after the definition 
# of a function,method,class,or module.

# Python doc attribute
# Whenever string literals are present
# just after the definition of a function,
# module,class or method,they are associated with 
# the object as their doc attribute.
# We can later use this attribute to 
# retrieve this docstring.

# It simply means that docstring can only be 
# printable as docstring if it given right below the function definition 
# or above the module

# PEP 8 
# PEP 8 is a document that provides guidelines and best practices on how to write python code.
# It was written in 2001 by guido van rossum,Barry Warsaw and Nick Coghlan.
# The Primary Focus of PEP 8 is to improve the readability and consistency of Python Code.

# PEP stands for Python Enhancement Proposal, and there are several of them.
# A PEP is a document that describes new features 
# proposed for python and documents aspects 
# of Python,Like Design and Style for the community.