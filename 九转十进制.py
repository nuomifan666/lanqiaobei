num=input()
ans=0
power=0
ls=[a for a in num[::-1]]
# print(ls)
for digit in ls:
    ans+= int(digit) *(9**power)
    power+=1
print(ans)
