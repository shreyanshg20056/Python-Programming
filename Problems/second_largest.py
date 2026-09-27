l = [1,4,6,3,8]
lar = l[0]
sec_lar = l[3]
for i in l:
  if i > lar:
    lar = i

for i in l:
  if i < lar and i > sec_lar:
    sec_lar = i

print(sec_lar)