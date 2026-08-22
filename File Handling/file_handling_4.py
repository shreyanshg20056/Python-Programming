# read() - reads the contemts of the file as str
# readline() -This read line by line and if you writes this command more than lines then it give you an empty string
file_handler = open("python13")

# fh = file_handler.read()
# fh = file_handler.read(10)  this reads first 10 characters of the file
# line1 = file_handler.readline()
# line2 = file_handler.readline()
# line3 = file_handler.readline() # Empty String - The file reached the file end of file

line1 = file_handler.readlines() # See,readlines() read line by line in a list and where readline() can only read one line at a time and for another line we have to write another line of readline() to print another line
file_handler.close()

# To print line by lines through readlines we can use loops
# To remove space from list occur by \n
for line in line1:
    print(line.rstrip('\n'))


# print(line1)
# print(type(line1))

# print(line2)
# print(line3) # an empty space of line