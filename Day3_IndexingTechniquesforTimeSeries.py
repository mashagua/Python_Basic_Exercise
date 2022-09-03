# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:06:30 2022

@author: masha
"""

"""
请你基于本节课所学的内容，编写相应的逻辑，针对本期课程中的数据框user_info，
在整个时间跨度内，逐月筛选出在当月进行注册的用户中，learn_time最长的用户其user_id及
对应的learn_time信息，形成新的数据框
"""
import pandas as pd
from datetime import datetime
data=pd.read_csv("Data/user_info.csv")
data['register_time']=pd.to_datetime(data['register_time'])

data['Y_M']=[datetime.strftime(ele,"%Y-%m") for ele in data["register_time"]]
sub_df=data.groupby(['Y_M'],as_index=False).agg({'learn_time':'max'})
longestlearn_df=sub_df.merge(data,how='left',
             left_on=["Y_M","learn_time"],
             right_on=["Y_M","learn_time"])

