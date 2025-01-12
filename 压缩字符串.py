'''
实现一个算法来压缩一个字符串。压缩的要求如下：

需要判断压缩能不能节省空间，仅在压缩后字符串比原字符串长度更短时进行压缩。

压缩的格式是将连续相同字符替换为字符 + 数字形式，例如 "AAABCCDDDD" 变为 "A3BC2D4"。

'''
def compress(s):
  if not s:
    return s
  str_list = []
  count = 1
  for i in range(1,len(s)):
    if s[i]==s[i-1]:
      count += 1
    else:
      str_list.append(s[i-1]+str(count) if count>1 else s[i-1])
      count = 1
  str_list.append(s[-1]+str(count) if count>1 else "")  # 最后一个字符
  return "".join(str_list) if len(str_list)<len(s) else s

print(compress(input())) # 输入字符串