# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 14:06:11 2022

@author: masha
"""

"""
请你基于本节课所学的内容，编写相应的逻辑，针对本期课程中的数据框btc，
计算最高价highp的30日周期同比涨幅（即(当日最高价-30日前最高价) / 30日前最高价），
对计算出的全部合法30日周期同比涨幅数据，逐月分组计算均值作为结果进行打印
"""
import pandas as pd
data = pd.read_csv('Data/BTC.csv', parse_dates=['date'], index_col='date')
data = data.assign(ratio=(
    data['highp']-data['highp'].shift(30, freq='D'))/data['highp'].shift(30, freq='D')).dropna()

data = data.reset_index()
ratio_bymonth = pd.DataFrame(data.resample('M', on='date').agg(
    average_ratio=pd.NamedAgg(column='ratio', aggfunc='mean')))
ratio_bymonth = ratio_bymonth.reset_index()
ratio_bymonth

