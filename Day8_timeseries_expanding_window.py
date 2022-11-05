"""
请你基于本节课所学的内容，编写相应的逻辑，针对附件中的天猫真实订单数据集tmall_order_report.csv，
统计出按订单创建时间顺序，总有效销售额（即买家实际支付金额不为0的记录）分别达到100000、500000、1000000时，
总订单数量、总有效订单数量、平均订单单价、最常出现的前3个收货地址、历经时长（单位：秒）等指标
"""
import matplotlib.pyplot as plt
import pandas as pd
tmall_data=pd.read_csv("Data/tmall_order_report.csv")
tmall_data=(tmall_data.query("买家实际支付金额>0").sort_values(by=["订单创建时间"]))
tmall_data.assign(lei=tmall_data.expanding(1)["买家实际支付金额"].sum())
satis_df_list=[tmall_data[tmall_data.expanding(1)["买家实际支付金额"].sum()<n] 
               for n in [100000,500000,1000000]]

all_info=[]
for df in satis_df_list:
    order_number=df.shape[0]
    avg_price=df['买家实际支付金额'].mean()
    max_address=' '.join(df['收货地址 '].value_counts().head(3).index)
    total_time=(pd.to_datetime(df["订单创建时间"]).max()-pd.to_datetime(df["订单创建时间"]).min()).total_seconds()
    all_info.append([order_number,avg_price,max_address,total_time])

all_info=pd.DataFrame(all_info,
                      columns=["总订单数量","平均订单单价","最常出现的前3个收货地址",
                               "历经时长"])