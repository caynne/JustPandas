# -*- encoding:utf-8 -*-
#有中文出现的情况，需要u'内容'
import json
import codecs
import sys
import PIL
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from configparser import ConfigParser
import sys
import cv2
import os
reload(sys)
sys.setdefaultencoding('utf-8')

'''
需求来源：帮老婆把每个月她们组员工的’日到访‘统计出来
日到访：每日到访的人数。可以将“首次拨打日期”字段统计出来就可以了
数据清洗：
    1、员人姓名，如：andy andy_zzp Andy_zzp等，统一为小写：andy
    2、日期，“首次拨打日期”字段的日期均需要提前一天，如：2017/2/3 ---> 2017/2/2
    3、
'''

#读入文件（我这台windows），目前这种方法不会有乱码。系统导出的文件，需要先另存为txt，然后将txt文件以utf8文件保存。
f = codecs.open(u'F:\code\pivot\资源统计表V1(2017.02.02--2017.03.01)utf8.txt',"r","utf8")

#pd1 = pd.read_csv(filepath_or_buffer = u'F:\code\pivot\data1.csv',encoding='utf8',skip_footer =4,header=8,engine='python')
df = pd.read_csv(filepath_or_buffer = f,
                 encoding='utf8',
                 engine='python',
                 sep='\t',
                 skip_footer=1)

#需要统计的员工
list = [
        'taylor',
        'cookie',
        'jerry',
        'star',
        'vincent',
        'yuria',
        'lemon',
        'phoebe'
]


frame = [] #定义一个列表存放用来concat的dataframe
for item in list:
    #将“推广员”字段均变为小写，再判断是否以xx开头
    subDf = df[df[u'推广员'].str.lower().str.startswith(item).fillna(False)]
    subDf[u'推广员'] = item
    frame.append(subDf)
result = pd.concat(frame)

#增加一列，方便做透视表。因为pivote在values跟columns是同一字段时会报错。
result[u'统计首次拨打日期'] = result[u'首次拨打日期']

#增加“修改首次拨打日期”列，因为按照需求，需要将“首次拨打日期”里的时间提前一天
def base_year(year):
    base_year = pd.Period(year)-1
    return base_year
result[u'修改首次拨打日期'] = result[u'首次拨打日期'].apply(base_year)

#生成透视表
pivotTable = pd.pivot_table(result,index=[u"推广员"],columns=[u'修改首次拨打日期'],values=[u'统计首次拨打日期'],aggfunc=u'count',fill_value=0)

#输入结果，写入result.csv文件
pivotTable.to_csv(u'F:/code/pivot/result.csv',mode='a',encoding ='gbk',sep=',')