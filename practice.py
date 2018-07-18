# l1=[1,2,3,4]
# from functools import reduce
# sumAll = reduce(lambda x,y :x+y , l1)
# print(sumAll)


# def addSum(a,b):
# 	print(a+b)
# addSum(10,20)

# l1=[1,2,3,4]
# l2=[10,20,30,40]
# associativeSum=list(filter(lambda a,b:a+b,l1,l2))
# print(associativeSum)



# for i in range(1,11):
# 	print("5 * %d =%d" %(i,5*i))

a=10
for i in range(1,a,2):
	print(" "*((a-i)//2)+"*"*i)