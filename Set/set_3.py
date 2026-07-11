# Intersection - &
sub_1 = {"English","Maths","Physics","Chemistry","CS"}
sub_2 = {"English","Biology","Physics","Chemistry"}
sub_3 = {"sanskrit","Maths","CS"}
common_subjects = sub_1.intersection(sub_2)
common_subjects1 = sub_2 & sub_3
print(common_subjects)
print(common_subjects1)

# Union - |
#Union_sub = sub_1.union(sub_2)
Union_sub = sub_1 | sub_2
print(Union_sub)

# difference of sets
week_days = {"Mon","Tue","Wed","Thurs","Fri","Sat","Sun"}
weekends = {"Sat","Sun"}
#weekdays = week_days - weekends
weekdays = week_days.difference(weekends)
print(weekdays)