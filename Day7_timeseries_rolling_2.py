"""
请你基于本节课所学的内容，编写相应的逻辑，针对本期课程中的数据框gold_price_daily，计算2003年内的记录中，
国际金价的5天、10天、30天、60天、120天及240天简单日均线以及对应的指数加权移动均线数据，
并基于pandas自带的plot()绘图方法将上述所有均线绘制出来，其中简单日均线用实线绘制，指数加权移动均线用虚线表示
"""
import pandas as pd
import matplotlib.pyplot as plt
gold_price_daily = pd.read_csv('Data/GPP_Model_2_Daily_Dataset.csv',
                               parse_dates=['Date'],
                               index_col='Date')

subset_after_2018 = (
    gold_price_daily
    .query('index >= "2018-01-01"')
)
fig, ax = plt.subplots()
(
    subset_after_2018
    .rolling(5)
    .mean()
    .rename(columns={'Price': 'rolling=5'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=5)
    .mean()
    .rename(columns={'Price': 'ewm_span=5'})
    .plot(ax=ax,style=':r')
)

(
    subset_after_2018
    .rolling(10)
    .mean()
    .rename(columns={'Price': 'rolling=10'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=10)
    .mean()
    .rename(columns={'Price': 'ewm_span=10'})
    .plot(ax=ax,style = '-',color='blue')
)

(
    subset_after_2018
    .rolling(30)
    .mean()
    .rename(columns={'Price': 'rolling=30'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=30)
    .mean()
    .rename(columns={'Price': 'ewm_span=30'})
    .plot(ax=ax,style='-',color='yellow')
)
(
    subset_after_2018
    .rolling(60)
    .mean()
    .rename(columns={'Price': 'rolling=60'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=60)
    .mean()
    .rename(columns={'Price': 'ewm_span=60'})
    .plot(ax=ax,style='-',color='green')
)

(
    subset_after_2018
    .rolling(120)
    .mean()
    .rename(columns={'Price': 'rolling=120'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=120)
    .mean()
    .rename(columns={'Price': 'ewm_span=120'})
    .plot(ax=ax,style='-',color='black')
)


(
    subset_after_2018
    .rolling(240)
    .mean()
    .rename(columns={'Price': 'rolling=240'})
    .plot(ax=ax)
)

(
    subset_after_2018
    .ewm(span=240)
    .mean()
    .rename(columns={'Price': 'ewm_span=240'})
    .plot(ax=ax,style='-')
)
plt.show()




