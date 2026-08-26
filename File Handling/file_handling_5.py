# 'a' mode => Append Mode
# we can use write() to use as append
#if the file does not exist a mode create a new file
fh = open("python16",'at')
fh.write("\nThis File Is Created Using 'a' mode")
fh.close()