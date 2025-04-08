#前缀项之和
def sum_array(n,A):
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]^A[i]
    total_sum=0
    for L in range(n):
        for R in range(L,n):
            total_sum+=prefix[R+1]^prefix[L]
    return total_sum

n=int(input())
A=list(map(int,input().split()))
print(sum_array(n,A))