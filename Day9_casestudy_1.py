"""
请你统计出2018-09-01当日，乘坐巴士与地铁各自的乘客数量（乘客数量：同一卡号当日至多记录1人）
由于一次完整的进出站记录由两条数据构成，那么请你针对原始数据中全量的地铁刷卡记录，从原始数据中针对卡号分组，
按时间顺序以及进出站的逻辑顺序，提取出每一条完整地铁出行记录
（处理过程中，若某条进站记录后紧接着无更晚的出站记录，或某条出站记录前紧接着无更早的进站记录，则舍弃此条记录），
将原始数据加工成具有卡号、进站时间、出站时间、进站站点、出站站点、进站线路名、
出站线路名字段的新的数据框shenzhen_metro_od
在shenzhen_metro_od数据框基础上，分别统计出2018-09-01早高峰时间段（早上7点半到9点半）内进站量top5站点、
出站量top5站点、进站->出站站点乘次top5组合
在shenzhen_metro_od数据框基础上，分别统计出2018-09-01早高峰时间段（早上7点半到9点半），跨线换乘记录中
（即进站线路名不同于出站线路名的记录），各线路之间跨线换乘组合即对应乘次统结果（降序排序，其中线路组合需保留顺序，
譬如地铁五号线->地铁一号线不同于地铁一号线->地铁五号线）
"""

import pandas as pd
from datetime import date
shenzhen_ic_records = pd.read_csv(
    'Data/深圳刷卡数据样本.csv',
    parse_dates=['deal_date'])
shenzhen_ic_records = shenzhen_ic_records.query(
    "deal_date.dt.date==@date(2018,9,1)")

shenzhen_ic_records = shenzhen_ic_records.assign(
    deal_type_new=[ele[:2] for ele in shenzhen_ic_records["deal_type"]])

shenzhen_ic_records.groupby(["deal_type_new"])["car_no"].nunique()
# 2
subway = shenzhen_ic_records.query("deal_type_new=='地铁'")
start = subway.query("deal_type=='地铁入站'").sort_values(
    by=["card_no", "deal_date"])
start = start[['card_no', 'deal_date', 'deal_type',
               'company_name', 'station', 'car_no']]
destination = subway.query("deal_type=='地铁出站'").sort_values(
    by=["card_no", "deal_date"])
destination = destination[['card_no', 'deal_date',
                           'deal_type', 'company_name', 'station', 'car_no']]
start.merge(destination, how="inner", left_on=["card_no"],
            right_on=["card_no"], suffixes=["_start", "_end"])
pd.merge_asof(start, destionation, on="deal_date", by="card_no")
