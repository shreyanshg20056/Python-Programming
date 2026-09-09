# 2nd Highest Value!!
scores = [2,45,64,103,4,8,14,47,45,90,2,0,1]
highest = scores[0]
highest_second = scores[2]
for score in scores:
    if score > highest:
        highest = score

    if score > highest_second & score < highest:
        highest_second = score
print(highest)
print(highest_second)