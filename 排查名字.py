n=int(input())
name=[]
for i in range(n):
    newname=input()
    if newname not in name:
        name.append(newname)
        print("NO")
    else:
        print("YES")
