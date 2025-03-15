import datetime

count = 0
start_date = datetime.date(1900, 1, 1)
end_date = datetime.date(9999, 12, 30)
date_delta = datetime.timedelta(days=1)

while start_date <= end_date:
    str_date = start_date.strftime('%Y%m%d')

    sum_year = sum(int(d) for d in str_date[:4])  # 年份数位和
    sum_month_day = sum(int(d) for d in str_date[4:6]) + sum(int(d) for d in str_date[6:])  # 月+日数位和

    if sum_year == sum_month_day:
        count += 1  # 符合条件的日期计数

    start_date += date_delta  # 递增一天

print(count)





# import os
# import sys
# import datetime
# from itertools import count
#
# count=0
# start_date = datetime.datetime(1900, 1, 1)
# end_date = datetime.datetime(9999, 12, 31)
# date_delta = datetime.timedelta(days=1)
# for i in range(1, 100000):
#     date = start_date + date_delta
#     str_date=date.strftime('%Y%m%d')
#     sumyear=0
#     summonth=0
#     for a in range (str_date[0],str_date[3]):
#         sumyear+=int(a)
#     for b in range (str_date[4],str_date[6]):
#         summonth+=int(b)
#     if sumyear==summonth:
#         count+=1
# print(count)