# Dictionary
# 
d = {
  "Name":"Shriyansh","Age":21
}
print(d)
print(d.keys())
print(d.values())
# print(d["N6ame"]) It returns error if key:value does not exist
print(d.get("N7ame"))#It returns no error if key:value does not exist

for key in d.keys():
  print(f"The Value Corresponding To The Key {key} is {d[key]}")

print(d.items)
for key,value in d.items():
  print(f"The Value Corresponding To The Key {key} is {value}")

