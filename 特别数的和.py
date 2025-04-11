n=int(input())
ans=0
for i in range(1,n+1):
    st=str(i)
    if st.count("2")==0 and st.count("0")==0 and st.count("1")==0 and st.count("9")==0:
        continue
    else:
        ans+=i
print(ans)