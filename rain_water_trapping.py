arr = [3,0,0,2,0,4]

ngr=[0]*len(arr)
ngl=[0]*len(arr)

ngl[0]=arr[0]
for i in range(1,len(arr)):
    ngl[i]=max(ngl[i-1],arr[i])

ngr[len(arr)-1]=arr[len(arr)-1]
for i in range(len(arr)-2,-1,-1):
    ngr[i]=max(ngr[i+1],arr[i])

total=0
for i in range(0,len(arr)):
    sums=min(ngr[i],ngl[i])
    total+=(sums-arr[i])
print(total)

