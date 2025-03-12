import os
import sys

# 请在此输入您的代码
import datetime

T = int(input())
start = datetime.datetime(1970, 1, 1, 0, 0, 0)
for i in range(T):
    strings = input().split()
    my_time = datetime.datetime.strptime(strings[0] + strings[1],"%Y-%m-%d%H:%M:%S")
    x = int(strings[2])
    # 求出所给时间与纪元时间的间隔
    delta_time = my_time - start
    # 求出间隔与x的取整，这一步是算纪元时间与所给时间之间有多少个x
    n = delta_time // datetime.timedelta(minutes = x)
    # 将 纪元时间 + n个x 即为最近的闹铃时间
    result = (start + n * datetime.timedelta(minutes = x)).strftime("%Y-%m-%d %H:%M:%S")
    print(result)