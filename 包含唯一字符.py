'''
确定字符串是否包含唯一字符

题目描述
实现一个算法来识别一个字符串的字符是否是唯一的（忽略字母大小写）。

若唯一，则输出YES，否则输出NO。

输入描述
输入一行字符串，长度不超过 100。

输出描述
输出一行，若字符串的字符是唯一的，则输出YES，否则输出NO。

'''

def is_unique(s):
    s = s.lower()
    char_set = set()
    for char in s:
        if char in char_set:
          return "NO"
        char_set.add(char)
    return "YES"

s = input()
print(is_unique(s))