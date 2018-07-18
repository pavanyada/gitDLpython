# 1) Write a program that checks whether the specified number is Armstrong number?

# num=input("Enter a number")
# sum=0

# length=len(num)
# num2=num
# if(num2>0)
# 	for i in range(0,length)
# 		temp=num2 % 10
# 		sum +=temp ** 3


# 2) Write a program to that checks the number is a prime or not?

# num=int(input("Enter a number "))
# count=0
# for i in range(1,num+1):
# 	if(num%i==0):
# 				count +=1
# if(count>2):
# 	print("%d is Composite Number" %(num))
# else:
# 	print(" %d is Prime Number" %(num))




# 3) Write a program for printing first 10 Fibonacci sequence?


# 4) Write a program for odd even count between range?

# num1=int(input("Enter First number"))
# num2=int(input("Enter First number"))
# counteven=0
# countodd=0
# for i in range(num1,num2+1):
# 	if(i%2==0):
# 		counteven +=1
# 		# print("%d is Even" %(i))
# 	else:
# 		countodd +=1
# 		# print("%d is odd" %(i))
# print("Total Even numbers are ",counteven)
# print("Total Odd numbers are ",countodd)		


# 5) Write a program for print the following pattern?
# *****
# ****
# ***
# **
#  *

# for i in range(5,0,-1):
# 	print('*' * i)



# 6) Write a program for multiples of 9 using if?



# 7) Write a program for printing numbers that are in the range between 1 to 50 and divisible by either 2 or 3?
# for i in range(2,50):
# 	if((i%2==0) or (i%3==0)):
# 		print(i)

# 8) Write a program to calculate sum of digits in number? 

num=input("Enter a number ")
number=0
length=len(num)
# int(number)
# int(num)
for i in range(0,length):
	number = number+int(num[i])

print("Sum of digits in the %s is %d" %(num,number))

