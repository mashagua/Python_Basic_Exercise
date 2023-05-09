from decimal import Decimal
print(0.1+0.2)
##去除不必要的浮点
print(Decimal('0.1')+Decimal("0.2"))


##统计多少个偶数
##type1:
numbers=[1,2,3,4,5,7,8,9]
count=0
for i in numbers:
    if i%2==0:
        count+=1
print(count)


##type2:利用bool值优化
count=sum(i%2==0 for i in numbers)


print(count)


##chek isdigit
print('123'.isdigit())
print(''.isdigit())


##
def extract_values(s):
    items=s.split(":")
    #因为s不一定会包含:,所以需要对结果进行判断
    if len(items)==2:
        return items[1]
    else:
        return ''

def extract_values_v2(s):
    return s.partition(":")[-1]

print('3$$$5'.split("$"))
print('3$$$5'.partition("$"))


##用户每日奖励积分数量
DAILY_POINTS_REWARDS=100
#VIP用户每日额外奖励积分的数量
VIP_EXTRA_POITS=20
##引入enum
from enum import Enum
#定义枚举类型时，若同时继承一些基础类型,比如int,str,在这里UserType可以当做int使用
class UserType(int,Enum):
    VIP=3
    BANNED=13
def add_daily_points(user):
    if user.type==UserType.BANNED:
        return
    if user.type==UserType.VIP:
        user.points+=DAILY_POINTS_REWARDS+VIP_EXTRA_POITS
        return
    else:
        user.points+=DAILY_POINTS_REWARDS
        return




