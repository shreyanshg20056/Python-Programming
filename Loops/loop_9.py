scores = [2,45,64,103,4,8,14,47,45,90,2,0,1]
# Lowest Value
lowest = scores[3]
for score in scores:
    if score < lowest:
        lowest = score
print(lowest)