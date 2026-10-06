# break terminates the iteration when the condition is met
for i in range(1,100):
  if i % 5 == 0:
    print(i)
    break

# continue skips the iteration when the condition is met.
for i in range(1,100):
  if i % 5 == 0:
    continue
  else:
    print(i)
