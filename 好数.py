n=int(input())
m=0
for i in range (1,n+1):
  while i>0 :
    if i%2!=0 :
      i=i//10
    else:
      break
    if i%2==0:
      i=i//10
    else:
      break
    if i==0:
      m+=1
print(m)