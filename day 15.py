"""
#Write a Python program to create a list of integers and print its elements.
li = [2,5,6,7,12,1,3,45,115]
print(li)

# Write a program to find the sum and average of all elements in a list. 
li = [2,5,6,7,12,1,3,45,115]
print(li)
print("Sum of list is ",sum(li))
print("avergare value ",sum(li)//len(li))


# Write a program to find the largest and smallest element in a list.

li = [2,5,6,7,12,1,3,45,115,-2]
print(li)
li.sort()
print("Smallest element is ",li[0])
print("Largest element is ",li[len(li)-1])

# Write a Python program to count the number of elements in a list without using len(). 

li = [2,5,6,7,12,1,3,45,115,-2]
print(li)
count =0
for i in li:
    count = count+1

print("Count is ", count)

# 5. Write a program to reverse a list without using built-in functions.

li = [2,5,6,7,12,1,3,45,115,-2]
print(li)
revlist = []
count = len(li)-1
while count>=0:
    revlist.append(li[count])
    count=count-1

print(revlist)

# Write a program to check if an element exists in a list.

li = [2,5,6,7,12,1,3,45,115,-2]
print(li)
num = int(input("Enter a number to search "))
if(li.count(num)>=1):
    print("Element exists")
else:
    print("Elemnt does not exist")

# Write a Python program to remove duplicate elements from a list. 
li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
print(li)

for i in li:
    if(li.count(i)>1):
        li.remove(i)
print(li)

# Write a program to sort a list in ascending and descending order.

li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

# Write a program to merge two lists and remove duplicates.

li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
secLi=[117,-2,-4,-56,-98,90,86,43]
print(li,secLi)
mergedList = li+secLi
for i in mergedList:
    if(mergedList.count(i)>1):
        mergedList.remove(i)
print(mergedList)

# Write a program to find common elements between two lists.
li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
secLi=[117,-2,-4,-56,7,45,5,-98,90,86,43]
print(li,secLi)
for i in li:
    for j in secLi:
        if(i==j):
            print(i, " is a commom element")
#  Write a program to split a list into even and odd numbers.

li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
print(li)
evenLi = []
oddLi = []
for i in li:
    if(i%2 == 0):
        evenLi.append(i)
    else:
        oddLi.append(i)
print(evenLi,oddLi)

#Write a Python program to find the second largest number in a list. 

li = [2,5,6,7,12,1,2,5,7,3,45,115,-2,-2,-2]
print(li)
li.sort(reverse = True)
print("Second largest number is ",li[1])
"""
# Write a program to flatten a nested list. 

nested_list = [1, [2,[10,11],3], [4,5], 6]
flat_list = []
for i in nested_list:
    if(type(i)== list):
        flat_list = flat_list+i
    else:
        flat_list.append(i)
print(flat_list)


























    


























































































