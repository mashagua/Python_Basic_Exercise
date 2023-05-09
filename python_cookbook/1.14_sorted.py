class User:
    def __init__(self,user_id):
        self.user_id=user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users=[User(23),User(3),User(99)]
print(sorted(users,key=lambda u:u.user_id))
from operator import attrgetter
print(sorted(users,key=attrgetter('user_id')))
##
mylist=[1,4,-5,10,-7,2,3,-1]
pos=(n for n in mylist if n>0)
print(pos)
for x in pos:
    print(x)
values=['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False

ivals=list(filter(is_int,values))
print(ivals)


addresses=["5412 N CLARK","5418 N CLARK","5800 E 58TH",
           "2122 N CLARK","6545 N R AVENSWOOD","1060 W ADDISON","4801 N BROADWAY"]
counts=[0,3,10,4,1,7,6]
from itertools import compress
more5=[n>5 for n in counts]
print(list(compress(addresses,more5)))