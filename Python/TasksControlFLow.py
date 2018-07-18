# 1) Write a program for printing number in the range excluding that are multiples of 3 and 5?

#num=int(input("Enter a number "))
# for i in range(1,11):
# 	if(i%3==0 or i%5==0):
# 		continue
# 	print("%d * %d = %d" %(num,i,num*i))

# # output:
# Enter a number 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 4 = 20
# 5 * 7 = 35
# 5 * 8 = 40


# 2) Write a program that prints only the even numbers squares in the specified range?

# start=int(input("Enter start number "))
# endp=int(input("Enter end point number "))
# for i in range(start,endp+1):
# 	if(i%2==0):
# 		print("%d is Even , So Square is %d" %(i,i**2))


# 3) Write a program that prints only the odd numbers that are divisible by 7 between 1
# to 100 using control flows?

# for i in range(1,101):
# i=0
# while(i<100):
# 	i+=1
# 	if(i%2==0):
# 		pass
# 	elif(i%7==0):
# 		print(i)




# 4) Write a program that print all vowels in the input string using control flow
# statements?
string=input("Enter a string")
for i in string:
	if(i is "a" or i is "e" or i is "i" or i is "o" or i is "u"):
		print(i)



