def decimal_to_base(n, base):
    """将十进制整数 n 转换为 base 进制（2-36）"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"

    result = ""
    sign = "-" if n < 0 else ""
    n = abs(n)

    while n:
        result = digits[n % base] + result
        n //= base

    return sign + result


# 示例：
print(decimal_to_base(255, 2))  # 输出: 11111111
print(decimal_to_base(255, 16))  # 输出: FF
print(decimal_to_base(-255, 8))  # 输出: -377
