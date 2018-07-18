# l1=[1,2,3,4]
# from functools import reduce
# sumAll = reduce(lambda x,y :x+y , l1)
# print(sumAll)


# def addSum(a,b):
# 	print(a+b)
# addSum(10,20)

l1=[1,2,3,4]
l2=[10,20,30,40]
associativeSum=list(filter(lambda a,b:a+b,l1,l2))
print(associativeSum)