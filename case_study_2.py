"""
请找出各个年龄段中，月均购买行为次数最多的前3名用户及其相应的月均购买行为次数
一件商品从曝光到被购买，最常见的时序链路是点击->添加到购物车->购买以及点击->购买，请你统计出不同性别下
（仅考虑男性/女性），这两种行为链路对应的商品成交量各自占比
任何一件商品从被用户点击，到后续一段时间内是否被购买都有着一定的转化率，若某件商品被某位用户点击后，
7天内发生对应的购买行为，则视作7日内完成转化（若按时间顺序连续出现某位用户针对某件商品的点击行为后再出现购买，
则只取第一条连续点击行为进行7日转化率的计算），请你统计出7日转化率最高的top10商品及其对应的7日转化率
"""
import pandas as pd
user_info = pd.read_csv('Data/用户信息采样.csv')
user_behavior = pd.read_csv("Data/用户行为采样.csv")
user_info_behavior = user_info.merge(user_behavior,
                                     how="left", on=['user_id'])
user_info_behavior = user_info_behavior.assign(time_stamp=[pd.Timestamp(
    "2021"+str(ele).zfill(4)) for ele in user_info_behavior["time_stamp"]])

user_info_behavior.groupby(['user_id'])
