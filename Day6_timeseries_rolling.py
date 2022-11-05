"""
请你基于本节课所学的内容，编写相应的逻辑，针对本期课程中的数据框gold_price_daily，计算2019年及以后记录中，
国际金价的5天、10天、30天、60天、120天及240天简单日均线（即每个交易日及以前N天之内价格的平均值），
并基于pandas自带的plot()绘图方法将各均线绘制出来，如附件中的output.png所示。
"""
import pandas as pd
import matplotlib
gold_price_daily = pd.read_csv('Data/GPP_Model_2_Daily_Dataset.csv',
                               parse_dates=['Date'],
                               index_col='Date')
# k:v的形式
rolling_dic = {f"{n}_day": lambda x, n=n: x['Price'].rolling(
    f"{n}D").mean() for n in [5, 10, 30, 60, 120, 240]}
gold_price_daily.sort_index().assign(**rolling_dic)
gold_price_daily.loc["2019-01-01":].plot(y=rolling_dic.keys())
