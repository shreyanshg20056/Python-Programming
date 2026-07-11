import copy
# shallow copy
l1 = [1,2.4,[10,20,30],'python']
l2 = copy.copy(l1)
l1[0] = 1000
l1[2][1] = 1000
print(l1,id(l1))
print(l2,id(l2))
# deep copy
l = [1,2.4,[10,20,30],'python']
l3 = copy.deepcopy(l)
l[0] = 1000
l[2][1] = 1000

print(l,id(l))
print(l3,id(l3))