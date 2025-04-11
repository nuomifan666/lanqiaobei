n=int(input())
w=map(int,input().split())
set1=set()
set1.add(0)
# for i in w:
#     for j in list(set1):
#         set1.add(j+i)
#         set1.add(abs(i-j))
for i in w:
    new_set = set()
    for j in set1:
        new_set.add(j + i)
        new_set.add(abs(j - i))
    set1.update(new_set)
print(len(set1)-1)
