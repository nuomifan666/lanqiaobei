s=input().lower()
counts=[0]*26
for i in s:
    if 'a' <= i <= 'z':  # 仅统计字母
        counts[ord(i)-ord('a')]+=1

max_count=max(counts)
for i in range(26):
    if counts[i]==max_count:
        print(chr(ord('a')+i))
        print(max_count)
        break