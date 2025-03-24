import os
import sys
def format2(n):
    formatstr = ""
    while n > 0:
        formatstr=str(n%2)+formatstr
        n=n//2
    return formatstr if formatstr else "0"


numcount=0
num=1
while numcount<23:
    if format2(num).count("1")==3:
        numcount=numcount+1
    num=num+1
print(num-1)