"""
For Loop Exercises
# 1. Print Numbers 
# Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print (i)

# Print Even Numbers 
# Print all even numbers between 1 and 20.
for i in range(1,21):
    if(i%2 == 0):
        print(i)
        
#Find Sum 
# Print the sum of numbers from 1 to 10 using a for loop.
sum = 0
for i in range (1,11):
    sum = sum+i
print("Sum of 1 to 10 is",sum)

#4. Multiplication Table 
# Take a number from the user and print its multiplication table up to 10. 
number = int(input("Enter a number between 1 to 10 "))
for i in range(1,11):
    print(number, " * ", i," = ",number*i)
print()

# Count Characters 
# Take a string and count the total number of characters using a for loop. 

count = 0    
uString = input("Enter your word ")
for i in uString:
    count = count+1
print("Characters count is ", count)

#6. Stop at 5 
#Print numbers from 1 to 10. 
#Stop the loop when the number becomes 5.
for i in range(1,11):
    print(i)
    if(i==5):
        break

#7. Search in List 
#Search for number 25 in a list. 
# If found, print "Found" and stop the loop.
numbers = [1,2,4,23,9,85,76,True,25,35]
isFound = False
for i in numbers:
    if(i==25):
        isFound = True
        break
if(isFound):
    print("Found")
else:
    print("Not Found")

#8. First Negative Number 
#Given a list of numbers, print the first negative number and stop the loop. 
numbers = [-2,1,2,4,23,-4,9,85,76,-5,25,35]
for i in numbers:
    if(i<0):
        print(i)
        break

#9. Skip 5 
#Print numbers from 1 to 10. 
#Skip number 5. 
for i in range(1,11):
    if(i==5):
        continue
    print(i)

#10. Skip Even Numbers 
#Print numbers from 1 to 20. 
#Skip all even numbers.
for i in range(1,21):
    if(i%2==0):
        continue
    print(i)
    
# 11. Skip Letter 
#Print each character of the string "PYTHON". 
#Skip the letter "O".
inputString = "PYTHON"
for i in inputString:
    if(i=="O"):
        continue
    print(i)

14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found". 

numbers = [1,2,4,23,9,85,76,25,35]
for i in numbers:
    if(i==100):
        print("Found")
        break    
else:
    print("not Found")
"""
# 15. Prime Number Check 
# Take a number from the user and check whether it is prime using for-else. 
num = int(input("Enter a number to check Prime or not "))
count = 0
for i in range (1,num+1):
    if(num%i==0):
        count = count +1
else:
    if(count==2):
        print("Prime")
    else:
        print("Not a Prime")
        
        



















