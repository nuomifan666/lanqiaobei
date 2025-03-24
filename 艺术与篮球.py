
import datetime
import time

a = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]  # 0-9 对应的笔画数
startday = datetime.date(2000, 1, 1)
endday = datetime.date(2024, 4, 13)
datedelta = datetime.timedelta(days=1)

res = 0
count = 0

while startday <= endday:
    str_day = startday.strftime("%Y%m%d")  # 计算当前日期的 8 位数字格式
    res = sum(a[int(d)] for d in str_day)  # 计算日期对应的笔画数
    if res > 50:
        count += 1
    startday += datedelta  # 日期加 1 天

print(count)








# import os
# import sys
# import datetime
# import time
#
# a = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]
# startday = datetime.date(2000,1,1)
# endday = datetime.date(2024,4,13)
# datedelta=datetime.timedelta(days=1)
# str_day=time.strftime("%Y%m%d")
# res=0
# count=0
# while startday<=endday:
#     res=sum(a[int(d)] for d in str_day)
#     if res>50:
#         count+=1
#     startday=startday+datedelta
# print(count)