import os
import sys
import datetime
count=0
start_day=datetime.date(2022,1,1)
end_day=datetime.date(2022,12,31)
delat_day=datetime.timedelta(days=1)
while start_day<=end_day:
    str_day=start_day.strftime('%Y%m%d')
    if start_day.weekday()==5 or start_day.weekday()==6 or str_day[-1]=="1" :
        count+=1
    start_day=start_day+delat_day

print(count)