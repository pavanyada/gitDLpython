l1=[1,2,3,4]
from functools import reduce
sumAll = reduce(lambda x,y :x+y , l1)
print(sumAll)