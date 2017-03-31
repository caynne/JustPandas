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

def do():
    f = codecs.open(u'F:\code\pivot\data.txt',"r","gbk")
    #pd1 = pd.read_csv(filepath_or_buffer = u'F:\code\pivot\data1.csv',encoding='utf8',skip_footer =4,header=8,engine='python')
    df = pd.read_csv(filepath_or_buffer = f,encoding='utf8',engine='python',sep='\t',)

    #生成透视表
    pivoTable = pd.pivot_table(df,index=[u"销售人员"],columns=[u'金额'],aggfunc='count')

    #结果输出到csv文件
    pivoTable.to_csv(u'F:/code/pivot/result.csv',encoding ='gbk',sep=',')
    pass
if __name__ == '__main__':
    do()
    pass