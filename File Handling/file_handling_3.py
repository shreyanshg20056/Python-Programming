# w mode - opens the file for writing. Overwrites the files
# if you use w mode when file does not exist then w mode creates a new file
fh = open("python13",'wt')
fh.write("This file is  overwritten using 'w' mode in python.\n")
fh.write("This file is created by default by w mode as it does not exist before then.")
fh.close()