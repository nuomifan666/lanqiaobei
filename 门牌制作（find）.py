count=0
for i in range(1,2021):
    s=str(i)
    pos=s.find("2")
    while pos!=-1:
        count+=1
        pos=s.find("2",pos+1)
print(count)