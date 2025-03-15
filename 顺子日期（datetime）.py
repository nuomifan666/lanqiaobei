import datetime

count = 0
start_time = datetime.datetime(2022, 1, 1)
start_delta = datetime.timedelta(days=1)

for i in range(365):
    start_time += start_delta  # 递增日期
    date_str = start_time.strftime("%Y%m%d")  # 转换为 "YYYYMMDD" 纯数字格式
    if "123" in date_str or "012" in date_str:  # 现在字符串格式正确
        count += 1

print(count)
