"""

# 1. Print numbers from 1 to 10 using a while loop.
a=1
while a<=10:
    print(a)
    a=a+1
# even numbers 1 to 20
a = 1
while a<=20:
    if a%2==0:
        print(a)
    a=a+1
# Odd numbers 1 to 20
a = 1
while a<=20:
    if a%2==1:
        print(a)
    a=a+1
# print numbers from 10 to1
a=10
while a>=1:
    print(a)
    a=a-1
#Print multiplication table of 5 using while loop.
a=1
while a<=10:
    print(5," * ",a," = ", 5*a)
    a=a+1
# Find the sum of first 10 natural numbers using while loop.
a=1
count =0
while a<=10:
    count = count +a
    a=a+1
print("Count of 1 to 10 is ",count)
# Find factorial of a number entered by user.
num = int(input("Enter a number "))
fact =1
while num>=1:
    fact = fact*num
    num = num-1
print("factorial is", fact)

#Count number of digits in a given number
num = int(input("Enter a number "))
count =0
while num>0:
    num = num//10
    count = count+1
print("Count of digits in the given number is ", count)

# Reverse a number using while loop.

num = int(input("Enter a number "))
reverse = 0
while num>0:
    reverse = reverse*10+num%10
    num = num//10
print("Reverse of a number is ",reverse)

# Ask user to enter password until correct password is entered.

password = "Sandy"
while True:
    userPassword = input("Enter the Password ")
    if(password == userPassword):
        userPassword = input("Access Granted")
        break
    else:
        userPassword = print("Password is incorrect. Please try again ")

# 14. Create a number guessing game: 
# • Generate a random number (1–10) 
# • Keep asking user until they guess correctly 
import random
    num = random.randint(1,10)
while True:
    uNum = int(input("Enter a number between 1 to 10 "))
    if num == uNum:
        print("You guessed the number correct ")
        break
    else:
        print("Guessed worn number try again ")
#15. Keep taking input numbers until user enters 0, then print total sum.
sumOfNum = 0
while True:
    number = int(input("Enter a number "))
    if(number == 0):
        break
    else:
        sumOfNum = sumOfNum+number
print("Sum of total numbers enetered is ",sumOfNum)

# 16. Print Fibonacci series up to N terms using while loop. 

n = int(input("Enter the number "))
count = 2
num1 = 0
num2 = 1
fSer = 0
print (num1, num2)
while count < n+1:
    fSer = num1+num2
    print(fSer)
    num1 = num2
    num2 = fSer
    count = count+1
"""






        

    
































































































