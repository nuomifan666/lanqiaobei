a,b,c,t=1,1,1,0
for i in range(4,20190325):
  t=(a+b+c)%10000
  a,b,c=b,c,t
print(c)