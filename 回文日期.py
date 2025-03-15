import datetime

def huiwen(date):
    return str(date) == str(date)[::-1]

def ababbaba(date):
    date_str = str(date)
    return (date_str[0] == date_str[2] == date_str[5] == date_str[7] and
            date_str[1] == date_str[3] == date_str[4] == date_str[6])

# 读取输入
date_str = input().strip()
year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:])
current_date = datetime.date(year, month, day)

# 找下一个回文日期
next_palindrome = current_date
while True:
    next_palindrome += datetime.timedelta(days=1)
    if huiwen(next_palindrome.strftime("%Y%m%d")):
        print(next_palindrome.strftime("%Y%m%d"))
        break

# 找下一个 ABABBABA 型回文日期
next_ababbaba = current_date
while True:
    next_ababbaba += datetime.timedelta(days=1)
    date_str = next_ababbaba.strftime("%Y%m%d")
    if huiwen(date_str) and ababbaba(date_str):
        print(date_str)
        break


#
# import datetime
#
# def huiwen(date):
#     return str(date) == str(date)[::-1]
#
# def ababbaba(date):
#     date_str = str(date)
#     if date_str[0] == date_str[2] == date_str[5] == date_str[7] and date_str[1] == date_str[3] == date_str[4] == date_str[6]:
#         return True
#     else:
#         return False
#
# date = input()  # ❌ 错误1：input() 得到的是字符串，无法直接进行日期运算
#
# while True:
#     ababbaba_date = date  # ❌ 错误2：直接将字符串赋值给变量，而后面试图进行日期计算
#     if ababbaba(ababbaba_date):
#         print(ababbaba_date)
#         break
#     else:
#         ababbaba_date += datetime.timedelta(days=1)  # ❌ 错误3：字符串不能直接加 timedelta，需要转换为 datetime.date 类型
#
# while True:
#     huiwen_ab_date = date  # ❌ 错误4：同样的问题，字符串不能直接用于日期计算
#     if huiwen(huiwen_ab_date) and ababbaba(huiwen_ab_date):
#         print(huiwen_ab_date)
#         break
#     else:
#         huiwen_ab_date += datetime.timedelta(days=1)  # ❌ 错误5：字符串不能直接加 timedelta，需要转换为 datetime.date 类型
