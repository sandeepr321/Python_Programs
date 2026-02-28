"""
add = 1
num = int(input("enter number for fact cal"))
for i in range(1,num+1):
    add = add*i
print("Factorial of a number is :", add)"""

num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if(i%3==0):
        count = count+1
print("Count of numbers divisible by 3 is ",count) 







