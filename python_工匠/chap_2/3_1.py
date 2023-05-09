from collections import namedtuple
from typing import NamedTuple
class Rectangle(NamedTuple):
    width:int
    height:int

rect=Rectangle(100,20)
print(rect)
movie={"name":"buring","type":"movie","year":2018}
##visit the key not exists
movie.get("rating",0)

d={"title":"foobar"}
##if items key not exists,return [],
d.setdefault("items",[]).append("foo")
print(d)
mm=d.setdefault("items",[]).append("bar")
print(d)
try:
    del d["ss"]
except:
    print("ss not in d.keys")
d.pop("ss",None)

##f
fru_1={"apple","orange","pineapple"}
fru_2={"tomato","orange","grapes","mango"}
print(fru_1&fru_2)
print(fru_1.intersection(fru_2))
##union
print(fru_2|fru_1)
print(fru_2.union(fru_1))
##difference
print(fru_2-fru_1)
print(fru_2.difference(fru_1))


##nonvariable is hashable,

##combine two dict
d1={"name":"apple.l"}
d2={"price":10}
##解包的过程是浅拷贝
print({**d1,**d2})
print([1,2,*range(3)])
nums=[10,2,3,21,10,3]
from collections import OrderedDict
print(list(OrderedDict.fromkeys(nums).keys()))


results=[]
for tasks_group in tasks:
    for task in tasks_group:
        if not (task.is_active() and task.has_completed()):
            continue
        if task.result_version==VERSION_2:
            result=task.result
        else:
            result=get_legancy_result(task)
        results.append(result)

def latlon_to_add(lat,lon):
    return coountry,province,city
##recursive new return value
##使用NamedTuple
from typing import NamedTuple
class Address(NamedTuple):
    country:str
    province:str
    city:str

def latlon_to_add(lat,lon):
    return Address(country=country,province=province,city=city)
##add new value distinct to Address,no need to modify the origin code
addr=latlon_to_add(lat,lon)
addr.country,addr.city
