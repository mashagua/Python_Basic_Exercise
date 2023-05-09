import heapq
nums=[1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
##使用在更复杂的结构上
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap=heapq.nsmallest(3,portfolio,key=lambda s: s["price"])
print(cheap)
#1.4.3寻找最大最小N个元素，同总数比，N很小，那么使用下面函数
heap=list(nums)
##转化为堆，push,pop复杂度都是O(logN)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
class PriorityQuene:
    def __init__(self):
        self._quene=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._quene,(-priority,self._index,item))



##1.6
from collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d=defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d=defaultdict(list)
for key,value in pairs:
    d[key].append(value)
