'''
问题描述
给定 n 个正整数 a1,a2,...,a”，你可以将它们任意排序。
现要将这 几 个数字连接成一排，即令相邻数字收尾相接，组成一个数。
问，这个数最大可以是多少。
输入格式
第一行输入一个正整数 n(1 < n < 20)。第二行输入 n 个正整数 a1,a2,·..,an(1 ≤ ai< 105)
输出格式
输出一个整数，表示答案。
'''

def largest_number(nums):
  str_nums = list(map(str, nums))
  for i in range (len(str_nums)):
    for j in range(i+1, len(str_nums)):
      if str_nums[i] + str_nums[j] < str_nums[j] + str_nums[i]:
        str_nums[i], str_nums[j] = str_nums[j], str_nums[i]

  result=''.join(str_nums)
  return result if result[0] != '0' else '0'

if __name__ == "__main__":
  n = int(input())
  nums = list(map(int, input().split()))
  print(largest_number(nums))