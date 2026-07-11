# Variable length arguments
# *args - variable length positional arguments (0 to n) -> *any_variable
# With this we can use function without using any variable such as sum can be done.It's I\O in tuple means it cannot be modified.

def add(*args):
    return sum(args)
result1 = add(1,3,7,36,9,6)
result2 = add() # The empty where no value passes gives output zero
print(result1)
print(result2)
