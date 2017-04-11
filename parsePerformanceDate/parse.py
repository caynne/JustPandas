# -*- encoding:utf-8 -*-
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

#有中文出现的情况，需要u'内容'C:\Users\Administrator\Desktop\手游性能\2.4.5\录屏.csv

reload(sys)
sys.setdefaultencoding('utf-8')

def go(newFile,oldFile):

    #读取csv文件，去掉前8行，以及最后4行。engine为python，不然为会警告
    pdOld = pd.read_csv(filepath_or_buffer = oldFile,
                          encoding = 'gbk',
                          skip_footer =4,
                          header=8,
                          engine='python')
    pdNew = pd.read_csv(filepath_or_buffer = newFile,
                          encoding = 'gbk',
                          skip_footer =4,
                          header=8,
                          engine='python')

    oldLable = oldFile.split('\\')[4]
    newLable = newFile.split('\\')[4]

    #内存占用均值
    memMeanOld = pdOld[u'应用占用内存PSS(MB)'].mean()
    memMeanOld = ("%.2f" % memMeanOld)

    memMeanNew = pdNew[u'应用占用内存PSS(MB)'].mean()
    memMeanNew = ("%.2f" % memMeanNew)

    #cpu占用均值
    cpuMeanOld = pdOld[u'应用占用CPU率(%)'].mean()
    cpuMeanOld = ("%.2f" % cpuMeanOld)

    cpuMeanNew = pdNew[u'应用占用CPU率(%)'].mean()
    cpuMeanNew = ("%.2f" % cpuMeanNew)

    #消电量
    batteryDiffOld =pdOld[u'电量(%)'].max()-pdOld[u'电量(%)'].min()
    batteryDiffNew =pdNew[u'电量(%)'].max()-pdNew[u'电量(%)'].min()

    #温度差
    tempDiffOld = pdOld[u'温度(C)'].max()-pdOld[u'温度(C)'].min()
    tempDiffOld = ("%.2f" % tempDiffOld)

    tempDiffNew = pdNew[u'温度(C)'].max()-pdNew[u'温度(C)'].min()

    plt.figure(num='astronaut',figsize=(10,8))

    plt.subplot(2,2,1) #左上展示mem对比图
    plt.plot(pdOld[u'应用占用内存PSS(MB)'],color="blue", linewidth=2.5, linestyle="-", label='old')
    plt.plot(pdNew[u'应用占用内存PSS(MB)'],color="red", linewidth=2.5, linestyle="-", label='new')
    plt.axis([0,200,50,200])
    plt.title("Mem+ High-definition+30mins")
    plt.legend(loc='lower right')

    plt.subplot(2,2,2)#右上展示cpu对比图
    plt.plot(pdOld[u'应用占用CPU率(%)'],color="blue", linewidth=2.5, linestyle="-", label='old')
    plt.plot(pdNew[u'应用占用CPU率(%)'],color="red", linewidth=2.5, linestyle="-", label='new')
    plt.title("Cpu+ High-definition+30mins")
    plt.legend(loc='lower right')


    plt.subplot(2,2,3)#左下展示电量消耗
    plt.plot(pdOld[u'电量(%)'],color="blue", linewidth=2.5, linestyle="-", label='old')
    plt.plot(pdNew[u'电量(%)'],color="red", linewidth=2.5, linestyle="-", label='new')
    plt.title("battery+ HighDefinition+30mins")
    plt.legend(loc='lower right')

    plt.subplot(2,2,4)#左下展示电量消耗
    plt.plot(pdOld[u'温度(C)'],color="blue", linewidth=2.5, linestyle="-", label='old')
    plt.plot(pdNew[u'温度(C)'],color="red", linewidth=2.5, linestyle="-", label='new')
    plt.title("temperature+ HighDefinition+30mins")
    plt.legend(loc='lower right')

    plt.show()
    return memMeanNew,memMeanOld,cpuMeanNew,cpuMeanOld,tempDiffNew,tempDiffOld,batteryDiffNew,batteryDiffOld

if __name__ == '__main__':
    newFile = unicode(raw_input(u'输入新版本文件路径\n'))
    oldFile = unicode(raw_input(u'输入旧版本文件路径\n'))

    memMeanNew,memMeanOld,cpuMeanNew,cpuMeanOld,tempDiffNew,tempDiffOld,batteryDiffNew,batteryDiffOld = go(newFile,oldFile)
    print '新版本内存均值%s' % memMeanNew
    print '旧版本内存均值%s' % memMeanOld
    print '新版本CPU均值%s' % cpuMeanNew
    print '旧版本CPU均值%s' % cpuMeanOld
    print '新版本耗电量%s' % batteryDiffNew
    print '旧版本耗电量%s' % batteryDiffOld
    print '新版本温度差%s' % tempDiffNew
    print '旧版本温度%s' % tempDiffOld

    pass