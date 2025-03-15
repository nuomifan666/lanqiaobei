import os
import sys
from datetime import date

# 请在此输入您的代码
info = input()
aa = int(info[:2])
bb = int(info[3:5])
cc = int(info[6:])
d = set()

def Year(y):
  return(1900+y if y >= 60 else 2000+y)

def D(a, b, c):
  year = Year(a)
  if 1960 <= year <= 2059:
    try:
      day = date(year, b, c)
      d.add(str(day))
    except:
      pass  # 忽略无效日期

D(aa,bb,cc)
D(cc,aa,bb)
D(cc,bb,aa)

d = list(d)
d.sort()
for j in d:
  print(j)
