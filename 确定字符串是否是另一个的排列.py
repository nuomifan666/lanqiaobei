'''
实现一个算法来识别一个字符串 str2 是否是另一个字符串 str1 的排列。排列的解释如下:如果将 str1 的字符拆分开，重新排列后再拼接起来，能够
得到 str2，那么就说字符串 str2 是字符串 str1的排列。(不忽略大小写)
如果 str2 字符串是 str1 字符串的排列，则输出 YES;如果 str2 字符串不是 str1 字符串的排列，则输出 NO;

'''
def is_permutation(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return "YES" if sorted(str1) == sorted(str2) else "NO"  # 排序后比较
str1=input()
str2=input()
print(is_permutation(str1, str2))