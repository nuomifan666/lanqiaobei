# 原始字符串
s = "WHERETHEREISAWILLTHEREISAWAY"

# 获取每个字符的 ASCII 码
ascii_values = [ord(c) for c in s]

# 按 ASCII 码排序
sorted_ascii_values = sorted(ascii_values)

# 将排序后的 ASCII 码转换回字符
sorted_chars = [chr(v) for v in sorted_ascii_values]

# 拼接成字符串
sorted_s = "".join(sorted_chars)

# 输出结果
print(sorted_s)

'''
s = "WHERETHEREISAWILLTHEREISAWAY"
sorted_s = "".join(sorted(s))
print(sorted_s)  # 输出：AAAEHIIILLRRRSWTTWY
'''