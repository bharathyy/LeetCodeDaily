arr = [1,3,-1,-3,5,3,6,7]
k=3
max_sum=float('-inf')

sum=0
n=0
for i in range(0,len(arr)):
    n+=1
    sum+=arr[i]
    if n==3:
        print(sum)
        max_sum = max(max_sum,sum)
        sum -= arr[i-k+1]
        n-=1
