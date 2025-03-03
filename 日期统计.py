from datetime import datetime, timedelta

st = '''5 6 8 6 9 1 6 1 2 4 9 1 9 8 2 3 6 4 7 7 5 9 5 0 3 8 7 5 8 1 5 8 6 1 8 3 0 3 7 9 2
7 0 5 8 8 5 7 0 9 9 1 9 4 4 6 8 6 3 3 8 5 1 6 3 4 6 7 0 7 8 2 7 6 8 9 5 6 5 6 1 4 0 1
0 0 9 4 8 0 9 1 2 8 5 0 2 5 3 3
'''
st = list(st.split())
#print(st)
dt1 = datetime(2023, 1, 1)#默认是2023-01-01 00：00：00
dt2 = datetime(2023, 12, 31)
res = 0
while dt2 >= dt1:
    date = dt1.strftime('%Y%m%d')#格式化成20230101这种格式
    num = 0
    for i in range(len(st)):
        if num == 8:#如果找到8位数字与当前日期相等res+1
            res += 1
            break
        if date[num] == st[i]:#枚举每一个数字找到相等的
            num += 1
    dt1 += timedelta(days=1)#日期加1
print(res)