# get()
marks = {'Math':60,'Phy':50,'Eng':64}
marks1 = {'Math':65,'Phy':50,'Eng':66}

print(marks.get('Phy'))
print(marks.get('chem',56)) #when we use print function for to get a key then there it occurs an error but if we use get() function then it occurs none output when on default given no value

# membership operator => in

print('Phy' in marks)

# update()
marks.update(marks1)
print(marks)
# pop()
marks.pop('Phy')
print(marks)
# keys cannot be duplicated in a dict
marks2 = {'Math':60,'Phy':50,'Eng':64,'Math':58}
print(marks2) # dict read from left to right so most recent key is the final key that its showing in output
