"""
请你基于本节课所学的内容，编写相应的逻辑，实现对附件中服务记录.xlsx数据记录中的服务记录水平进行统计，具体统计规则：
　　每一行记录为一次服务的发起及结束时间，当服务发起时间位于晚上8点到早上8点之间时，视作夜班单，
这种情况下当服务耗时低于30分钟记作优秀单，耗时在30~60分钟记作合格单，超过60分钟记作不合格单；
当服务发起时间位于早上8点到晚上8点之间时，视作白班单，这种情况下当服务耗时低于15分钟记作优秀单，
耗时在15~30分钟记作合格单，超过30分钟记作不合格单

请分别统计出整体三个水平服务单的各自比例、夜班单三个水平服务单的各自比例、白班单三个水平服务单的各自比例
"""
import pandas as pd
from datetime import datetime


def count_percentage(datafile):
    data = pd.read_excel(datafile)
    data["hour"] = [datetime.strptime(
        ele, "%Y年%m月%d日%H点%M分%S秒").hour for ele in data["服务发起时间"]]
    data['班次'] = ["夜单" if (ele >= 20 or ele < 8)
                  else "白单" for ele in data["hour"]]
    start_list = [datetime.strptime(i, "%Y年%m月%d日%H点%M分%S秒")
                  for i in data["服务发起时间"]]
    end_list = [datetime.strptime(i, "%Y年%m月%d日%H点%M分%S秒")
                for i in data["服务结束时间"]]
    data["cost_time"] = [(ele1-ele2).total_seconds() /
                         60 for (ele1, ele2) in zip(end_list, start_list)]
    data['label'] = ["优秀" if ((data["班次"].iloc[i] == "白单" and data["cost_time"].iloc[i] < 15) or (data["班次"].iloc[i] == "夜单" and data["cost_time"].iloc[i] < 30)) else "不合格" if (
        (data["班次"].iloc[i] == "白单" and data["cost_time"].iloc[i] > 30) or (data["班次"].iloc[i] == "夜单" and data["cost_time"].iloc[i] > 60)) else "合格" for i in range(len(data))]

    freq_df = data.groupby(['班次'])['label'].value_counts().unstack().fillna(0) 
    pct_df = freq_df.divide(freq_df.sum(axis=1), axis=0)
    return pct_df

if __name__ == "__main__":
    datafile = "Data/服务记录.xlsx"
