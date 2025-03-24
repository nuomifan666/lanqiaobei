string = input()
stack = []
seen = set()

for char in string:
    if char in seen:
        continue  # 跳过重复字符
    seen.add(char)
    stack.append(char)

result = ''.join(stack)
print(result)










# string = input()
# stack = []
#
# for char in string:
#     if stack and stack[-1] == char:
#         stack.pop()  # 移除连续字母对
#     else:
#         stack.append(char)
#
# result = ''.join(stack)
# print(result)


# string = input()
# char_list = list(string)
#
# index = 0
# while index < len(char_list) - 1:
#     if char_list[index] == char_list[index + 1]:
#         del char_list[index:index + 2]  # 删除连续字母对
#         index = max(0, index - 1)  # 退一步，重新检查
#     else:
#         index += 1
#
# result = ''.join(char_list)
# print(result)
