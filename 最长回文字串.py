s = input().strip()
n = len(s)
if n == 0:
    print(0)
else:
    max_len = 1  # 至少一个字符时，最长回文子串长度为1

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 计算有效回文长度

    for i in range(n):
        len1 = expand(i, i)    # 奇数长度
        len2 = expand(i, i + 1)  # 偶数长度
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
    print(max_len)