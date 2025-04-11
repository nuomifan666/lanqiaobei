import datetime

# 定义1970年1月1日00:00:00作为起始时间
start = datetime.datetime(year=1970, month=1, day=1)

# 定义一个毫秒级的时间增量
dela = datetime.timedelta(milliseconds=1)

# 获取用户输入的毫秒数
now = int(input())

# 计算从1970年1月1日00:00:00开始经过now毫秒后的时间
now = start + now * dela

# 使用字符串格式化输出时分秒，不足两位数前面补0
# print(f'{now.hour:02d}:{now.minute:02d}:{now.second:02d}')

now_time=now.strftime("%H:%M:%S")
print(now_time)