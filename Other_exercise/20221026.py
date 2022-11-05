"""
1、同一卡号在同一店铺内进行消费，并且订单金额一样。
2、订单来源不一致（根据订单号判断，一共有3个来源，订单号分别以4200、010、11703_comsume开头）
满足上述两种条件即判断为重复积分，需要将重复积分的数据按卡号展示出来。
"""
import pandas as pd
data=pd.read_excel('Data/服务记录.xlsx')
print(data.head())
sel_data=(
    data.loc[data.duplicated(subset=["卡号","订单金额"])]
)