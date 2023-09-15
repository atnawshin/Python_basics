#set
set1 = {1,2,5,3,6}
set2 = set([2,5,3,7,8,9])
set1.add(7)
set2.remove(9)
print(2 in set1)
print(2 not in set2)
print(set1 | set2) #union
print(set1 & set2) #intersection
print(set1 - set2) #difference

'''#set e items er kono order thake na so index er maddhome access kora jay na ar kono duplicate value rakha jabe na
set1 = {1,3,4,6,8,2,5}
set2 = set([1,3,6,2,4,7,9,5])
#set1.add(9)
#set2.remove(6)
print(set1 | set2) #union
print(set1 & set2) #intersection
print(set1 - set2) #difference - set1 theke je value gula set2 te ache ta minuse korbo
#print(4 in set1)
#print(3 not in set2)'''