import datetime

# 使用 datetime 库
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 10, 1)
delta = datetime.timedelta(days=1)
total_km = 0

while start_date <= end_date:
    km = 1
    if start_date.weekday() == 0 or start_date.day == 1:
        km = 2
    total_km += km
    start_date += delta
print(total_km)
