#1.2从任意长度的可迭代对象中分解元素
import numpy as np
def avg(series):
    return np.mean(series)
def drop_first_last(grades):
    first,*middle,last=grades
    return avg(middle)
record=("Dave","dave@example.com","773-555-1212","847-555-1212")
name,email,*phone_number=record
*trailing,current=[10,7,8,1,9,5,10,3]
trailing_avg=sum(trailing)/len(trailing)
print(trailing_avg)


record=[('foo',1,2),
        ('bar','hello'),
        ('foo',3,4)]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*arg in record:
    if tag=='foo':
        do_foo(*arg)
    elif tag=='bar':
        do_bar(*arg)
#1.3 保存最后N个元素

from collections import deque
##当发现有匹配时输出当前的匹配行以及最后检查过的N行文本
#处理搜索过程的代码使用搜索过程的代码解耦
def search(lines,pattern,history=5):
    previous_line=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_line
        previous_line.append(line)

print(deque([1,2,3,4,5],maxlen=6))


#
q=deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
print(q)
#右边删除
q.pop()
print(q)
if __name__=="__main__":
    with open("data/somefile.txt") as f:
        for line,prevlines in search(f,"python",5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print("-"*20)
