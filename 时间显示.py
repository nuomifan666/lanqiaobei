from datetime import datetime, timedelta

# 定义1970年1月1日00:00:00作为起始时间
start = datetime(year=1970, month=1, day=1)

# 定义一个毫秒级的时间增量
dela = timedelta(milliseconds=1)

# 获取用户输入的毫秒数
now = int(input())

# 计算从1970年1月1日00:00:00开始经过now毫秒后的时间
now = start + now * dela

# 使用字符串格式化输出时分秒，不足两位数前面补0
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second)) 
