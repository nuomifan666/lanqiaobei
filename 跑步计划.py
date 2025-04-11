import datetime
total=0
date1=datetime.date(2023,1,1)
date2=datetime.date(2023,12,31)
while date1<date2:
    if date1.weekday()==0 or date1.month==1 or date1.month==10 or date1.month==11  or date1.day==1 or date1.day==11\
            or date1.day==31 or date1.day==11:
        total=total+5
    else:
        total+=1
    date1+=datetime.timedelta(days=1)
print(total)