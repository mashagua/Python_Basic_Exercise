
'''请你基于本节课所学的内容，编写一个功能函数get_max_duration()，
传入原始日期时间字符串列表参数datetime_string_list，格式规则列表参数datetime_format_list，
它们的长度需要一一对应，通过编写相应的计算逻辑，输出时间间隔最大的成对原始日期时间字符串及对应的时间差（单位：秒）'''
import time
from datetime import datetime


def get_max_duration(datetime_string_list, datetime_format_list):

    format_time = [datetime.strptime(i, j) for (i, j) in zip(
        datetime_string_list, datetime_format_list)]
    sorted_time_tuple = sorted(zip(format_time, datetime_string_list))
    return {"涉及原始日期时间": [sorted_time_tuple[-1][1], sorted_time_tuple[0][1]], "时间差(秒)": (sorted_time_tuple[-1][0]-sorted_time_tuple[0][0]).total_seconds()}


if __name__ == "__main__":
    test_imput1 = [
        '2001-01-15 12:22:00',
        '2010年4月27日5点28分08秒',
        '20190122134528',
        '2018年7月17日15点03分02秒',
        '2022/03/06 17:42:15'
    ]
    datetime_format_list = [
        "%Y-%m-%d %H:%M:%S",
        "%Y年%m月%d日%H点%M分%S秒",
        "%Y%m%d%H%M%S",
        "%Y年%m月%d日%H点%M分%S秒",
        "%Y/%m/%d %H:%M:%S"
    ]
    get_max_duration(test_imput1, datetime_format_list)
