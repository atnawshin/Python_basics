list = [[2,[3,8,88],5],56,3,75,35,88,46,35,2,85,48,97,"Hello"] #nested list
print(list[0][1][2]) #1st one access the 1st element fro the main list and second one accessing the first element of the second list
list.append(90)#addes an item to the end of the list
print(list)
list.insert(2,99)
print(list)
list.extend([0,1,2])
print(list)
list = list + [6,7,8]
print(list)
list.remove(1) #remove the exact item
print(list)
list.pop() #remove the last item of the list
print(list)
list.remove(list[4]) #remove from the index
print(list)
list1 = [6,2,7,1,4,2,7,8]
list1.sort()
print(list1)
list2 = ["ad","kjhg","djkhg"]
list2.sort()
print(list2)
print(list.index(6))
print(list.count(2))
