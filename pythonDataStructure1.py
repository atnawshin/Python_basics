#Linear search
'''
def linear_search(arr, n, item):
    for i in range (0,n):
        if (arr[i]==item):
            return i
    return -1
arr = [10,2,4,6,-7,8]
n = len(arr)
item = -7

index = linear_search(arr,n,item)
if(index==-1):
    print("Item not found")
else:
    print("Item found at index ",index)
'''

#binary search
a = [1,4,5,6,35,76,88,97,134]
item = 97

left = 0
right = len(a) - 1
while(left<=right):
    middle = (left+right)//2 ##'//' is used to get floor ans
    if(a[middle] == item):
        print("Item found at index ",middle)
        exit()
    elif(a[middle] < item):
        left = middle + 1
    else:
        right = middle - 1
print("Item not found.")