subjects = ["C","C++","JAVA","Python","Basics"]
print(len(subjects))
subjects.append("TOC") #add item at last position
subjects.insert(3,"JAVAScript") #add item in the given position
#subjects.remove("TOC")
subjects.sort() #sorted according to dictionary order
print(subjects)
subjects.reverse()
print(subjects)
pos = subjects.index("JAVA")
print(pos)
count = subjects.count("JAVA")
print(count)
numbers = [20,1,6,4,75,94,335,38,28,47,23]
print("Length of the list: ",len(numbers))
numbers.sort()
print("Sorted numbers",numbers)
#numbers.reverse()
#print(numbers)
numbers.pop() #last item removed
print("After pop:",numbers)
numbers3 = numbers.pop()
print("poped item:",numbers3)
print(numbers)
#numbers.clear() #clear all items
numbers2 = numbers.copy()
print("Copy of list in numbers2  = ",numbers2)

pos = numbers.index(4) #returns the position of the item -query for the particular item
count = numbers.count(4) #how many times the item has appared -query for the particular item
print(pos)
print(count)