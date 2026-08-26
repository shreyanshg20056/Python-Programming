# with statement:It automatically closes the file before it terminates the program
with open("python66","xt") as fh:
    content = fh.write("This File is created in with statement.")

print(content)