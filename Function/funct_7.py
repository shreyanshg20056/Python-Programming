# Variable length arguments
# **kwargs - Variable length keyword arguments - dict type
#*args comes before **kwargs
def student_details(sname, **marks):
    if len(marks) == 0:
        print(f"{sname} is absent!")
    else:
        percent = sum(marks.values())/len(marks)
        print(f"Congrats!! {sname} got {percent} achieved")
    print(marks)
student_details('John', sub1 = 80.3, sub2=76.8,sub3=88.1)
student_details('Rick', sub1 = 86.3, sub2=74.4,sub3=85.1)