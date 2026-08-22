# Creating a file
fh = open("python12",'xt')

# Writing into a file
# write(content)
fh.write("This file is created using the 'x' mode in Python.\n ")
fh.write("Next line.")

# Closing the file
fh.close() # After closing the file we cannot perform any operations
