# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:31:41 2022

@author: masha
"""
"""
请你基于本节课所学的内容，编写相应的逻辑，
针对本期课程中的数据框user_info，去除所有无最近登录时间的记录后，
统计出每个月内注册用户中，当月流失用户与非当月流失用户各自的数量与占比，
并按照当月流失占比对最后的结果倒序排序，其中当月流失指该用户的
register_time与recently_logged同年同月
"""

import pandas as pd
from datetime import datetime
pd.set_option("display.max_columns", None)
data = pd.read_csv("Data/user_info.csv")

data['register_time'] = pd.to_datetime(data['register_time'], errors='coerce')
data['recently_logged'] = pd.to_datetime(
    data['recently_logged'], errors='coerce')

data = data[~pd.isna(data["recently_logged"])]


resample_groups = list(data.resample('M', on='register_time'))
# 查看regis时间==recent时间

total_2 = data.assign(user_passed=data["register_time"].dt.to_period("m") == (data['recently_logged'].dt.to_period("m"))).groupby(
    [pd.Grouper(key='register_time', freq='MS'), 'user_passed']).agg(
        user_passed_true=pd.NamedAgg(column='user_passed', aggfunc='count'))

total_2 = total_2.reset_index()
total_2['user_passed_true_percentage'] = total_2.groupby(
    ['register_time'])["user_passed_true"].transform(lambda x: x/x.sum())

total_2.resample('MS', on='register_time').apply(
    lambda df: pd.DataFrame(df).sort_values('user_passed_true', ascending=False))
