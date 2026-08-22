# Opening a File in Python - open(file_name,mode_to_open)
# Modes: r,x,w,a,b,t
# Default Modes: rt

file_handler = open("practice.txt",'rt')
print(file_handler)

# Closing a file
file_handler.close()
file_handler.close()
print(file_handler)
# we can close file as many times as it takes, but it did'nt give us any errors