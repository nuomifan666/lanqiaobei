import os
import sys

# 请在此输入您的代码
def special_Value(n):
  if n.count('1') == 3 or n.count('2') == 3:      #月份里符合条件的特殊值只有‘0’、‘1’。
    return True
  return False

def common_Value(x, y, z):        #判断此时间是否有共同的特殊值
  a = sorted(x)
  b = sorted(y)
  c = sorted(z)
  if a == b == c:
    return True
  return False

years = []
for year in range(0,10000):
  t = "%04d" % (year)      #将数据转换为所需格式
  if special_Value(t):
      years.append(t)

mouths = []
for mouth in range(1,13):
  for day in range(1,31):
    q = "%02d%02d" % (mouth, day)      #将数据转换为所需格式
    if special_Value(q):
      mouths.append(q)

times = []
for hour in range(0,24):      #0不可能符合条件
  for minute in range(0,60):
    p = "%02d%02d" % (hour, minute)     #将数据转换为所需格式
    if special_Value(p):
      times.append(p)

sum = 0
for a in years:
  for b in mouths:
    for c in times:
      if common_Value(a, b, c):
        sum += 1
print(sum)